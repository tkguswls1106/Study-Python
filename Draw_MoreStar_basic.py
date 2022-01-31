for i in range(5):  #줄 개수
        for j in range(5):  #별 개수
                if j<=i:  #for in range문이니 j가 0부터 4까지 늘어날테니까,
                          #if문으로 제한을 걸어둠
                        print('*', end='')
        print()  #print문은 파이썬에선 기본적으로 엔터기능이 탑재되어있음.
