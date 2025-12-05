import logging
import platform
import time

logger = logging.getLogger("AmeliaSystem")

def system_diagnostic():
    """Performs a mock system diagnostic."""
    logger.info("Initiating system diagnostic sequence...")
    time.sleep(0.5)
    
    sys_info = {
        "System": platform.system(),
        "Node": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    
    for key, value in sys_info.items():
        logger.info(f"{key}: {value}")
        time.sleep(0.1)
        
    logger.info("Diagnostic sequence completed successfully.")
    return True