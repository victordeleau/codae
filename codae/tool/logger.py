# set the logging environment

import logging
import sys
import datetime
import torch

"""
    setup logging capabilities
"""
def set_logging(log_file_path="/mnt/ramdisk/", log_file_name=None, logging_level=logging.INFO):

    now = datetime.datetime.now()
    log_file_name = ("CODAE_" + now.strftime("%Y-%m-%d %H:%M") + ".log" if log_file_name == None else log_file_name)

    root = logging.getLogger()
    root.setLevel(logging_level)

    # send logging stream to stdout as well
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(logging_level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    sh.setFormatter(formatter)
    root.addHandler(sh)

    # try to add log output file
    try:
        fh = logging.FileHandler( log_file_path + log_file_name )
        fh.setLevel(logging_level)
        root.addHandler(fh)
    except:
        logging.error("Couln't create log file %s" %(log_file_path + log_file_name) )

    return logging

    
def display_info(config):

    print("")
    logging.info("### LEARNING RATE = %f" %config["MODEL"]["LEARNING_RATE"])
    logging.info("### WEIGHT DECAY = %f" %config["MODEL"]["WEIGHT_DECAY"])
    logging.info("### NB EPOCH = %d" %config["MODEL"]["EPOCH"])
    logging.info("### BATCH SIZE = %d" %config["MODEL"]["BATCH_SIZE"])
    logging.info("### NB INPUT_LAYER = %d" %config["MODEL"]["NB_INPUT_LAYER"])
    logging.info("### NB OUTPUT LAYER = %d" %config["MODEL"]["NB_OUTPUT_LAYER"])
    logging.info("### STEEP LAYER SIZE = %d" %config["MODEL"]["STEEP_LAYER_SIZE"])
    logging.info("### EMBEDDING SIZE = %d" %config["DATASET"]["EMBEDDING_SIZE"])
    logging.info("### Z SIZE = %d" %config["MODEL"]["Z_SIZE"])
    logging.info("### IO SIZE = %d" %(len(config["DATASET"]["USED_CATEGORY"])*config["DATASET"]["EMBEDDING_SIZE"]))
    logging.info("### NB CATEGORY = %d\n" %(len(config["DATASET"]["USED_CATEGORY"])))