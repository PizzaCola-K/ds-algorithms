# Save the Prisoner!

[HackerRank](https://www.hackerrank.com/challenges/save-the-prisoner/problem)

n명의 사람, m개의 사탕을 s번째 사람부터 시작해서 나줘줄 때, 마지막에 받는 사람 찾기

n명의 사람을 0, 1, 2 ... n - 1 번 자리에 앉힌다.

5명을 기준으로 해서

1개의 사탕을 0번째 자리부터 준다고 하면 0번 자리,

2개의 사탕을 0번째 자리부터 준다고 하면 1번 자리,

...

5개 사탕을 0번째 자리부터 주면 4번 자리

6개의 사탕을 주면 0번 자리

...

m개의 사탕을 0번째 자리부터 주면 (m - 1) % 5 자리이다.

0번째 자리부터 주는것을 1, 2, 3번 자리부터 준다고 하면,

m - 1 + 1,2,3,...,이 되서 이는 (m - 1) + (s - 1)이 된다.

그러므로 마지막 사탕을 받는 자리는 ((m - 1) + (s - 1)) % n 이 되며

사람으로 따지면 윗값의 +1이다.