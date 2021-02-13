int d[-100..100]={0...0};

read(n);

for i=1..n{
  read(x);
  d[x]=d[x]+1;
}

for x=-100..100{
  for i=1..d[x]{
    write(x, ' ');
  }
}