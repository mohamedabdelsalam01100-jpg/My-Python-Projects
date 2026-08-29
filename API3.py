logs = [
    "INFO: User Ahmed logged in",
    "ERROR: Database connection failed",
    "WARNING: Password expires soon",
    "ERROR: Invalid user ID",
    "INFO: User Sara logged in",
    "ERROR: Database connection failed",
    "INFO: User Omar logged in",
]
def analyze(logs):
    errors = []
    error_n = 0
    info_n = 0
    warning_n = 0
    for log in logs:
        if log.startswith("INFO"):
            info_n+=1
        elif log.startswith("ERROR"):
            error_n+=1
            error_message = log.replace("ERROR: ","")
            if error_message not in errors:
                errors.append(error_message)
        elif log.startswith("WARNING"):
            warning_n+=1
        
    return{"INFO":info_n,
                "ERROR":error_n, 
                "WARNING":warning_n,
                "ERRORS":errors}
print(analyze(logs))


        
