def filter_by_location(job_postings, location):
    return [job for job in job_postings if job['location'] == location] 
