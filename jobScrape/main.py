from scrapy import cmdline
import arrow
#script for easier PyCharm debugging

def main():
    command = "scrapy crawl socareers -o jobs" + arrow.now().format('YYYY-MM-DD') + ".json"
    #print(command)
    cmdline.execute(command.split())

if __name__ == "__main__":
    main()
