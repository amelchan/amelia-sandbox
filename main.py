import argparse
import logging
import platform
import sys
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
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

def main():
    parser = argparse.ArgumentParser(description="Amelia Intelligence Augmentation - System CLI")
    parser.add_argument("--diagnostic", action="store_true", help="Run system diagnostic")
    parser.add_argument("--status", action="store_true", help="Check system status")
    parser.add_argument("--version", action="store_true", help="Show version information")
    
    args = parser.parse_args()
    
    logger.info("Amelia System CLI initialized.")
    
    if args.version:
        print("Amelia Core v2.4.0 (Stable)")
        return

    if args.diagnostic:
        system_diagnostic()
    elif args.status:
        logger.info("System Status: OPTIMAL")
        logger.info("All subsystems functioning within normal parameters.")
    else:
        logger.warning("No directive specified. Use --help for usage information.")

if __name__ == "__main__":
    main()