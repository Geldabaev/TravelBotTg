from crontab import CronTab

cron = CronTab(user='runas')

job1 = cron.new(command='python /home/runas/PycharmProjects/pythonProject2/lists_news.py')

job1.minute.every(1)

job2 = cron.new(command='python /home/runas/PycharmProjects/pythonProject2/lists_news.py')
job2.every(1).minute()

for item in cron:
    print(item)

cron.write()