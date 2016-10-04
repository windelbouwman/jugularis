module crt;


function void exit()
{
    syscall(60, 0, 0, 0);
}

function void print(string a)
{
  var int i;
  for (i=0; i< a->len; i = i+1)
  {
     putc(a->txt[i]);
  }
}


function void putc(byte ch)
{
  syscall(1, 1, cast<int>(&ch), 1);
}

function void syscall(int a, int b, int c, int d);

