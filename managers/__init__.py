"""COMET Managers

IntentHash¹¹: 0x9E5C3A7D_P3_1_COMET_MANAGERS_20260303T0308Z

Core managers for browser automation.
"""

from .daemon_manager import DaemonManager
from .skill_manager import SkillManager
from .session_manager import SessionManager

__all__ = ['DaemonManager', 'SkillManager', 'SessionManager']
