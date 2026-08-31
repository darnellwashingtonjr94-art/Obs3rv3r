import pytest
from backend.verification.evaluator import OutputValidator

def test_output_validator_init():
    validator = OutputValidator()
    assert validator.self_verifier_models is not None
