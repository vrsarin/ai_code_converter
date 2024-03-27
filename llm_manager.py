"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python
from langchain_openai import ChatOpenAI
from langchain.llms.ollama import Ollama
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_text_splitters import RecursiveCharacterTextSplitter

from constants import DEFAULT_CHUNK_SIZE
from converter_context import ConverterContext
from llm_types import LlmTypes
from utils import save_to_file


class LlmManager:
    """This class abstracts LLM functionality and provide generic functions"""
    __llm: any
    __context: ConverterContext

    def __init__(self,
                 context: ConverterContext
                 ) -> None:
        self.__context = context
        self.__get_llm()

    def __get_llm(self) -> any:
        match self.__context.llm_type:
            case LlmTypes.OPENAI:
                self.__llm = ChatOpenAI(model_name='gpt-4-0125-preview',
                                        streaming=True,
                                        callbacks=[
                                            StreamingStdOutCallbackHandler()],
                                        temperature=0)
            case LlmTypes.LLAMA2:
                self.__llm = Ollama(model="llama2:70b",
                                    callbacks=[
                                        StreamingStdOutCallbackHandler()],
                                    temperature=0)

    def __get_prompt(self, prompt: str) -> str:
        sys_start_token = ""
        sys_end_token = ""
        user_start_token = ""
        user_end_token = ""
        src = self.__context.source.value
        dest = self.__context.target.value
        match self.__context.llm_type:
            case LlmTypes.LLAMA2:
                sys_start_token = "<<SYS>>"
                sys_end_token = "<</SYS>>"
            case LlmTypes.OPENAI:
                sys_start_token = "SYSTEM:"
                sys_start_token = "USER:"
            case _:
                sys_start_token = "USER:"

        return f"""{sys_start_token}You are an expert in {src} and {dest} programming languages!!
{prompt}
{sys_end_token}

{user_start_token}
**{src} Source Code**:
""" + "{input}\n" + user_end_token

    def extract_information(self,
                            prompt: str,
                            content: str,
                            file_name: str):
        """Extract information using LLM"""
        extraction_chain = LLMChain.from_string(llm=self.__llm,
                                                template=self.__get_prompt(prompt))
        return_value = extraction_chain.invoke({"input": content})
        save_to_file(return_value['text'], file_name)

    def extract_information_chunked(self,
                                    prompt: str,
                                    content: str,
                                    file_name: str,
                                    chunk_size: int = DEFAULT_CHUNK_SIZE,
                                    chunk_overlap: int = 0):
        """Extract information using LLM"""
        extraction_chain = LLMChain.from_string(llm=self.__llm,
                                                template=self.__get_prompt(prompt))
        code_splitter = RecursiveCharacterTextSplitter.from_language(
            language=self.__context.source,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap)

        documents = code_splitter.split_text(content)
        for doc in enumerate(documents):
            return_value = extraction_chain.invoke({"input": doc})
            save_to_file(return_value['text'], file_name)
