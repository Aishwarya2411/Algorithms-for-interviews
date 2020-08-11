class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        let_logs=[]
        dig_logs=[]
        for log in logs:
            if log.split()[1].isnumeric():
                 dig_logs.append(log)
            else:
                let_logs.append(log)
       

        let_logs.sort(key=lambda a : (a.split()[1:],a.split()[0]))
        
        return (let_logs+dig_logs)
