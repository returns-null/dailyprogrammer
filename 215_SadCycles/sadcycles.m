function sadcycles ()

  b = input('');
  n = input('');

  function sum = termNext(ne)
    sum = 0;
    while ne > 0
        sum = sum + floor(mod(ne,10))^b;
        ne = ne / 10;
    end
  end

  tortoise = n;
  hare = n;

  while 1
    tortoise = termNext(tortoise);
    hare = termNext(termNext(hare));
    if (tortoise == hare)
      break;
    end
  end

  while 1
    fprintf(1,num2str(tortoise));
    tortoise = termNext(tortoise);
    if (tortoise == hare)
      fprintf(1,'\r\n');
      break;
    end
    fprintf(1,', ');
  end

end