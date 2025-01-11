#!/usr/bin/env python3
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # Expect 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Expect 0
