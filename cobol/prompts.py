"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python

from enum import Enum


class CobolPrompts(Enum):
    """Prompts that we will use to generate programs"""

    SUMMARY = """Write a detailed document explaining the business logic in plain English using the provided "COBOL code," so any programmer can understand it.
Follow the below rules for extraction:
    - Differentiate between paragraphs and sections
    - Include PROGRAM-ID and Program-Names if possible
    - Explain each COBOL word in plain English

DO NOT INCLUDE THE CONCLUSION!!"""

    PROCEDURE = """Write a detailed implementation logic in PSUEDOCODE format. provide your output in format as described in "output format" section.

Follow the below rules for extraction:
- Section contains Paragraphs
- Paragraph contains Sentences
- Sentenced contains Statements
- Statements contain Phrases
- When any empty Section, Paragraph, Sentence, Statement, Phrase do not include it in output but follow identation rule
- when SQL execution if found write exact sql being executed
- Refer to **Keyword Mapping Table** when determining output text
- Use the **Keyword Mapping Table** as reference only as WS-VAR, WS-SENDING-VAR, WS-COUNTRY-CODE, WS-RECEIVING-VAR, WS-FULL-PHN-NBR are sample not exact
- When **COBOL VARIABLE** is found, use "Declare Variable" instead of "Define"
- When explaining anything add it as a COMMENT
- when starting new paragraph add a line "end of paragrapah" above your output
- when end the output add a line "end of section"
- donot include any markdown in output

Keyword Mapping Table:
| Cobol | Output |
| ----- | ------ |
| SKIP1 | Insert single blank line |
| SKIP2 | Insert two blank lines |
| SKIP3 | Insert three blank lines |
| INITIALIZE WS-VAR | Initialize variable WS-VAR |
| MOVE WS-SENDING-VAR TO WS-RECEIVING-VAR | Assign WS-RECEIVING-VAR = WS-SENDING-VAR  |
| MOVE WS-COUNTRY-CODE  TO WS-FULL-PHN-NBR(1:2) | Assign WS-FULL-PHN-NBR[0 to 1] = WS-COUNTRY-CODE |
| PERFORM Z-200-GET-PROCESS-DATE | Call method Z-200-GET-PROCESS-DATE() |
| Evaluate SQLCODE |  Switch Case SQLCode |
| Perform SQL-INITIAL until SQL-INIT-DONE | Call methods from SQL-INITIAL till SQL-INIT-DONE in sequence (need attn.) |
| Call 'DSNHLI' using SQL-PLIST25 | Call method DSNHLI (by value SQL-PLIST25) |
| Call 'DFHEI1' using by content and by reference WS-ABCODE | Call method DSNHLI (by reference WS-ABCODE) |
| GO TO SQL-INIT-END. | Call method SQL-INIT-END() |

Output Format:
Section: **Section**
    Paragraph: **Paragraph**        

"""

    DATA = """Extract ER Diagram from the given COBOL Source Code for Oracle RDBMS. provide your output in table format as described in "output format" section.

Follow the below rules for extraction:
- include the precisions 
- ignore comments as they can be misleading
- include Table Name, Attribute Name, Data Type, Precision
- also refer Data Table when determining Data Type
- write reltions in freeform and assume best format from best practices

**DATA TYPE TABLE**:
| COBOL | DATA TYPE | PRECISION |
| ----- | --------- | --------- |
| PIC S9(4) USAGE IS BINARY | NUMERIC | |
| PIC S9(9) USAGE IS BINARY | NUMERIC | |
| COMP-1 | REAL or FLOAT | |
| COMP-2 | DOUBLE PRECISION or FLOAT | |
| S9(i)V9(d) COMP-3 or S9(i)V9(d) PACKED-DECIMAL | DECIMAL or NUMERIC | i+d,d |
| S9(i)V9(d) DISPLAY SIGN LEADING SEPARATE | DECIMAL or NUMERIC | i+d,d |
| S9(i)V9(d) NATIONAL SIGN LEADING SEPARATE | DECIMAL or NUMERIC | i+d,d |
| S9(4) COMP-4, S9(4) COMP-5, S9(4) COMP, or S9(4) | BINARY or SMALLINT | |
| S9(9) COMP-4, S9(9) COMP-5, S9(9) COMP, or S9(9) | BINARY or INTEGER | |
| S9(18) COMP-4, S9(18) COMP-5, S9(18) COMP, or S9(18) | BINARY or BIGINT | |
| SQL TYPE is BINARY(n) | BINARY | n     |
| SQL TYPE is VARBINARY(n) | VARBINARY | n     |
| USAGE IS SQL TYPE IS BLOB(i) | BLOB | i     |
| USAGE IS SQL TYPE IS CLOB(i) | CLOB | i     |
| USAGE IS SQL TYPE IS DBCLOB(m) | DBCLOB | m     |
| SQL TYPE IS XML AS BLOB(i) | XML | |
| SQL TYPE IS XML AS CLOB(i) | XML | |
| SQL TYPE IS XML AS DBCLOB(i) | XML | |
| SQL TYPE IS ROWID | ROWID | |


Output Format:
**Table Name**:
| Attribute Name | Data Type | Precision | Key |

**Relations**:


"""

    CODE = """
Write Java Code from the given psuedo code extracted from COBOL Source Code.

Follow the below rules for extraction:
- in case of ambiguity call it out in output
- treat section akin classes
- treat paragraph akin methods

"""
