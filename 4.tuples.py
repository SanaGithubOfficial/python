{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e0e6d941-19fa-449b-b9f6-b07cbb8949a3",
   "metadata": {},
   "source": [
    "\n",
    "### Tuples in python\n",
    "* ___tuples are immutable lists cannot be changed in any way once it is created.___\n",
    "* ___tuples are defined in the same way as lists.___\n",
    "* ___They are enclosed within parenthesis and not within square braces.___\n",
    "* __similar to string indices , the first value in the tuples will have the index[0], the second value is [1].__\n",
    "* ___tuples are ordered , indexed collections of data.___\n",
    "* ___negative indices are counted from the end of the tuples, just like lists___\n",
    "* ___tuples can store duplicate values___\n",
    "* ___tuples allow you to store several data items including string, integer,,float in one variable___"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b9dd102b-2837-4037-a666-345006383884",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "() <class 'tuple'>\n"
     ]
    }
   ],
   "source": [
    "#creating empty tuple\n",
    "x=()\n",
    "print(x,type(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "55d11f08-176e-4e0b-b01e-eee57625a789",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1] <class 'list'>\n"
     ]
    }
   ],
   "source": [
    "x1=[1]\n",
    "print(x1,type(x1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b611f521-2dd0-4308-b3b1-2081c08dc523",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python\n",
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "x2=(\"python\")\n",
    "print(x2)\n",
    "print(type(x2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1222d8e1-3519-4f84-86a8-86cf1e02ccd4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('hello world',\n",
       " 'python',\n",
       " 3.147,\n",
       " 10,\n",
       " True,\n",
       " False,\n",
       " ('harry', 55, True, 'False'),\n",
       " {10, 20},\n",
       " {'a': 'apple', 'b': 'boy'})"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup1=('hello world','python',3.147,10,True,False,(\"harry\",55,True,'False'),{10,10,20},{\"a\":\"apple\",\"b\":\"boy\"})\n",
    "tup1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "582f1b5f-7ea5-4c9c-b072-c8f1501a3918",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n",
      "{'a': 'apple', 'b': 'boy'}\n"
     ]
    }
   ],
   "source": [
    "#accessing their values\n",
    "print(tup1[0])\n",
    "print(tup1[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1431a471-ccba-428a-a13d-a0e91bdca538",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('hello world',\n",
       " 'python',\n",
       " 3.147,\n",
       " 10,\n",
       " True,\n",
       " False,\n",
       " ('harry', 55, True, 'False'),\n",
       " {10, 20},\n",
       " {'a': 'apple', 'b': 'boy'})"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#slicing of tuple\n",
    "tup1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "05f6cee8-ff02-45fc-b417-18c79eef241a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('hello world',\n",
       " 'python',\n",
       " 3.147,\n",
       " 10,\n",
       " True,\n",
       " False,\n",
       " ('harry', 55, True, 'False'),\n",
       " {10, 20},\n",
       " ['komal', 'kartik', 100])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup1=('hello world','python',3.147,10,True,False,(\"harry\",55,True,'False'),{10,10,20},['komal','kartik',100])\n",
    "tup1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "78633c74-1cbb-4b47-a824-8440801a2dbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('hello world',\n",
       " 'python',\n",
       " 3.147,\n",
       " 10,\n",
       " True,\n",
       " False,\n",
       " ('harry', 55, True, 'False'),\n",
       " {10, 20},\n",
       " ['komal singh', 'kartik', 100])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup1[8][0]=\"komal singh\"\n",
    "tup1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f5278b98-b99a-4e12-b293-7f93d2ff5e5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('hello world',\n",
       " 'python',\n",
       " 3.147,\n",
       " 10,\n",
       " True,\n",
       " False,\n",
       " ('harry', 55, True, 'False'),\n",
       " {10, 20},\n",
       " ['komal singh', 'kartik', 100])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#slicing of tuple\n",
    "tup1=('hello world',\n",
    " 'python',\n",
    " 3.147,\n",
    " 10,\n",
    " True,\n",
    " False,\n",
    " ('harry', 55, True, 'False'),\n",
    " {10, 20},\n",
    " ['komal singh', 'kartik', 100])\n",
    "tup1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dd7c9b19-0657-417f-8c89-964c3b92e715",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(True, 'False')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup1[6][2:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "626f8e6a-f616-4e18-81b6-4a68b7a998f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100.25,\n",
       " 'hello world',\n",
       " True,\n",
       " False,\n",
       " [[['ganesh'], [['sujit']]]],\n",
       " (20,\n",
       "  40,\n",
       "  True,\n",
       "  False,\n",
       "  ((20, ['komal singh', [[[[[[['pyhton']], 'sana']]]]]]), 'kartik', 'rohit'),\n",
       "  'shahid'))"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2=(100.25,'hello world',True,False,[[['ganesh'],[['sujit']]]],(20,40,True,False,(((20,[\"komal singh\",[[[[[[[\"pyhton\"]],\"sana\"]]]]]]),((\"kartik\")),(\"rohit\"))),((\"shahid\"))))\n",
    "tup2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c5c003e1-8569-44fd-9e0a-98ab5719b5a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[['ganesh'], [['sujit']]]]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "98af0dd1-1340-46e3-b664-8b74c935c371",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['ganesh'], [['sujit']]]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[4][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6bdf67a8-e7c7-4bf2-9443-5d57feaf7871",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['sujit']]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[4][0][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "feb27734-6a0e-4d02-8229-9d8e7be4a310",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['sujit']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[4][0][1][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "0c77163e-d1f0-4706-92d3-e3f75e4714c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'sujit'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[4][0][1][0][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "19ae5564-e78b-42c4-9e3d-8b2299897d23",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100.25,\n",
       " 'hello world',\n",
       " True,\n",
       " False,\n",
       " [[['ganesh'], [['sujit']]]],\n",
       " (20,\n",
       "  40,\n",
       "  True,\n",
       "  False,\n",
       "  ((20, ['komal singh', [[[[[[['pyhton']], 'sana']]]]]]), 'kartik', 'rohit'),\n",
       "  'shahid'))"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "aaea4582-c6ed-4f59-8603-10296b7938de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'komal singh'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[5][4][0][1][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "b0ec3011-665d-40e0-9e91-d050ce81ceaf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'pyhton'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[5][4][0][1][1][0][0][0][0][0][0][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "fbe1e695-5b57-4002-9213-0a9c7dbe5094",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'sana'"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[5][4][0][1][1][0][0][0][0][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "7e25e7c0-67af-4ffe-8fa3-c782d9383a9c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'kartik'"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[5][4][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "7ec45bcd-1e4d-4429-bdc3-59025c3c2843",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'rohit'"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[5][4][2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "9071e5c5-494b-423e-a5a7-f4e57418dfb7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'shahid'"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[5][5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "bd789705-906d-455f-bfff-2c2e0c2d70f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ganesh'"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup2[4][0][0][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "db1bc1ad-f955-490d-b327-94bcefb7711c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('hello world', True, 'python', 'ganesh', False)\n"
     ]
    }
   ],
   "source": [
    "#concatenation of tuples\n",
    "tup1=(\"hello world\",True)\n",
    "tup2=(\"python\",\"ganesh\",False)\n",
    "tup3=tup1+tup2\n",
    "print(tup3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "75a3d247-7b2c-4365-80a3-a5f5566d3bba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 6, 6, 6, 6, 564, 9, 464, 64, 646, 46, 46, 4, 1, 2, 3, 4, 5, 6, 6, 6, 6, 564, 9, 464, 64, 646, 46, 46, 4)\n"
     ]
    }
   ],
   "source": [
    "rep_tup=(1,2,3,4,5,6,6,6,6,564,9,464,64,646,46,46,4)\n",
    "print(rep_tup*2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "27acae28-112b-461d-be12-863eb0d0f46d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "#membership operator in not in\n",
    "rep_tup\n",
    "print(10 in rep_tup)\n",
    "print(6 not in rep_tup)\n",
    "print(6 in rep_tup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "3e27c772-fb73-4cca-9b60-d83741f05e8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 2, 3, 4, 5, 6, 6, 6, 6, 564, 9, 464, 64, 646, 46, 46, 4)"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#agrigate function\n",
    "#min(),max(),len(),count(),sum()\n",
    "rep_tup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "eeb9af80-ce71-4f29-8164-40f3bc3e5b86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count total: 4\n",
      "minimum value: 1\n",
      "maximum value:646\n",
      "lenght of numbers:17\n",
      "sum of the value:1882\n"
     ]
    }
   ],
   "source": [
    "print(f\"count total: {rep_tup.count(6)}\")\n",
    "print(f\"minimum value: {min(rep_tup)}\")\n",
    "print(f\"maximum value:{max(rep_tup)}\")\n",
    "print(f\"lenght of numbers:{len(rep_tup)}\")\n",
    "print(f\"sum of the value:{sum(rep_tup)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "9e6fded6-92f7-4a4a-b554-e5a0f9723aeb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('k', 'o', 'm', 'a', 'l', ' ', 's', 'i', 'n', 'g', 'h')"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# tup(seq) function\n",
    "# It converts a specific squence to a tuple\n",
    "seq=\"komal singh\"\n",
    "tuple(seq)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "311f8ca9-62ea-4e6f-abb6-e016c040f29a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 6, 6, 6, 6, 564, 9, 464, 64, 646, 46, 46, 4)\n"
     ]
    }
   ],
   "source": [
    "print(rep_tup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "c4388f6f-2625-453f-af6a-793d2f20aa71",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 9, 46, 46, 64, 464, 564, 646]"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tuple_3= sorted(rep_tup)\n",
    "tuple_3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "e3dd69d0-5d0d-4d5c-a433-e248fe543654",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[646, 564, 464, 64, 46, 46, 9, 6, 6, 6, 6, 5, 4, 4, 3, 2, 1]"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tuple4= tuple_3[::-1]\n",
    "tuple4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "6f6e3c42-c9d1-4d21-a732-551dfe2f1a9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 2, 3, 4, 5, 6, 6, 6, 6, 564, 9, 464, 64, 646, 46, 46, 4)"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# tuples are immutable datatype\n",
    "rep_tup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "971503e4-3c65-4c35-9c59-a985b3bf0af7",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'tuple' object has no attribute 'append'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[87]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[43mrep_tup\u001b[49m\u001b[43m.\u001b[49m\u001b[43mappend\u001b[49m(\u001b[33m\"\u001b[39m\u001b[33mhello world\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[31mAttributeError\u001b[39m: 'tuple' object has no attribute 'append'"
     ]
    }
   ],
   "source": [
    "rep_tup.append(\"hello world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "b84ff935-5b4b-442d-a0bd-36ed8084c815",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'tuple' object has no attribute 'extend'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[88]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[43mrep_tup\u001b[49m\u001b[43m.\u001b[49m\u001b[43mextend\u001b[49m(\u001b[32m1\u001b[39m)\n",
      "\u001b[31mAttributeError\u001b[39m: 'tuple' object has no attribute 'extend'"
     ]
    }
   ],
   "source": [
    "rep_tup.extend(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "04713d39-9c9d-43ee-8d6b-df6d9c1c96fa",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'tuple' object has no attribute 'insert'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[89]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[43mrep_tup\u001b[49m\u001b[43m.\u001b[49m\u001b[43minsert\u001b[49m(\u001b[32m49\u001b[39m)\n",
      "\u001b[31mAttributeError\u001b[39m: 'tuple' object has no attribute 'insert'"
     ]
    }
   ],
   "source": [
    "rep_tup.insert(49)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "77c4ed81-f920-4de5-a9fa-92bb7cef5c31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 2, 3, 4, 5, 6, 6, 6, 6, 564, 9, 464, 64, 646, 46, 46, 4)"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#update\n",
    "rep_tup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "88c55e2c-4bd6-45cb-8fac-40e2c8ab8ce2",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[91]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[43mrep_tup\u001b[49m\u001b[43m[\u001b[49m\u001b[32;43m0\u001b[39;49m\u001b[43m]\u001b[49m=\u001b[32m100\u001b[39m\n\u001b[32m      2\u001b[39m rep_tup\n",
      "\u001b[31mTypeError\u001b[39m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "rep_tup[0]=100\n",
    "rep_tup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "814b5aca-f9a7-490b-aa48-4573c036d4ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 2, 3, 4, 5, 6, 6, 6, 6, 564, 9, 464, 64, 646, 46, 46, 4)"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#delete\n",
    "rep_tup\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "3bee27eb-75da-49c6-a37d-c18395c5deb8",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object doesn't support item deletion",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[93]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mdel\u001b[39;00m(\u001b[43mrep_tup\u001b[49m\u001b[43m[\u001b[49m\u001b[32;43m0\u001b[39;49m\u001b[43m]\u001b[49m)\n",
      "\u001b[31mTypeError\u001b[39m: 'tuple' object doesn't support item deletion"
     ]
    }
   ],
   "source": [
    "del(rep_tup[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "b29d5804-b369-4b84-9ff0-a16902bc2141",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "shahid shaikh\n"
     ]
    }
   ],
   "source": [
    "txt='shahid shaikh'\n",
    "print(txt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "7ff112a5-7315-4c94-9c60-766161dd2376",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'SHAHID SHAIKH'"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "txt.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a86008af-6594-4702-bd13-74cdc7c58177",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
