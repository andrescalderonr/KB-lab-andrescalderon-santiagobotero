from enum import Enum

class Value(Enum):
    """
    Semantic representation of truth-values used in the logical language.

    This enumeration defines the three possible evaluations that a
    proposition of the system may take:

       - TRUE:     The proposition is evaluated as true.
       - FALSE:    The proposition is evaluated as false.
       - UNKNOWN:  The truth value cannot be determined within
                   the system (e.g., incomplete information).

    These values are intended to be used in:
       - semantic evaluation of formulas,
       - multi-valued logic operations,
       - game states or knowledge-based systems where uncertainty is present.

    Attributes
    ----------
    TRUE : int
       Represents logical truth, encoded as integer 1.
    FALSE : int
       Represents logical falsehood, encoded as integer 2.
    UNKNOWN : int
       Represents an indeterminate or undefined truth value, encoded as integer 3.
    """
    TRUE = 1
    FALSE = 2
    UNKNOWN = 3