# Copyright 2020 Diogo Coelho
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#Standard library imports
from random import randint

# Third party imports
import pyperclip as clip

CHARLIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZqwertyuiopasdfghjklzxcvbnm,.;<>:?{[}]1234567890-=!@#$%¨&*()_+°£"

def main():
    key = ''
    x = input('Size: ')
    for i in range(int(x)):
        next = randint(0, CHARLIST.__len__()-1)
        key = key + CHARLIST[next]

    clip.copy(key) 

if __name__=="__main__":
    main()
