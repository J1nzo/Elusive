import urllib

def main():
    # Server behind cloudflare, can't download file
    # content = urllib.urlopen('http://a.pomf.se/jufvrx.txt').read()
    words = open('jufvrx.txt', 'r').read().strip().split('\n')
    answer = ''
    N = 1
    while 2**N<=len(words):

        answer+= words[(2**N)-1][0]
        N+=1
    print 'Answer:', answer

if __name__ == "__main__":
    main()
