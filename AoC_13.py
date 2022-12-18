{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "3bdf22d9-7324-4a03-957a-d8775edcda2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "file = r\"C:\\Users\\Di\\Downloads\\Input_13.txt\"\n",
    "with open(file) as f:\n",
    "    data = f.readlines()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "9c79c851-dd1c-4d36-9cb2-7453780d6426",
   "metadata": {},
   "outputs": [],
   "source": [
    "def right_order(left, right):\n",
    "\n",
    "    if isinstance(left, int):\n",
    "        if isinstance(right, int):\n",
    "            if left < right:\n",
    "                return True\n",
    "            elif left > right:\n",
    "                return False\n",
    "            elif left == right:\n",
    "                return None\n",
    "        \n",
    "        else:\n",
    "            return right_order([left], right)\n",
    "    else:\n",
    "        if isinstance(right, int):\n",
    "            return right_order(left, [right])\n",
    "        else:\n",
    "            if left == right:\n",
    "                return None\n",
    "            \n",
    "            if len(left) == 0 and len(right) > 0:\n",
    "                return True\n",
    "            elif len(left) > 0 and len(right) == 0:\n",
    "                return False\n",
    "            elif len(left) == 0 and len(right) == 0:\n",
    "                return None\n",
    "            \n",
    "            for i in range(min(len(left), len(right))):\n",
    "                \n",
    "                if right_order(left[i], right[i]) is not None:\n",
    "                    return right_order(left[i], right[i])\n",
    "                \n",
    "            if left == right:\n",
    "                return None\n",
    "            return len(left) < len(right) \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "686eb08b-c647-4ccc-b1c7-effb75eedf30",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5393"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total = 0\n",
    "\n",
    "for idx in range(int(len(data)/3)):\n",
    "    left = eval(data[3 * idx])\n",
    "    right = eval(data[ 3* idx + 1])\n",
    "    total += (1 + idx) * right_order(left, right)\n",
    "\n",
    "total    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "bbdcf1fe-33dd-437e-a129-d23fe24558c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1], 5] [[1], 4]\n",
      "[1] [1]\n",
      "5 4\n",
      "5 4\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "left = [[1], 5] #eval(data[3])\n",
    "right = [[1], 4] #eval(data[4])\n",
    "right_order(left, right)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "44c06fe7-12e8-4a2f-adcb-9a87be145b5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "left == right"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "01004eb6-9d3d-4500-a4fb-7618b7414ce8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "060cabb5-a7e4-4796-919c-a8ef13f8d3e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "26712"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count_1 = 0\n",
    "count_2 = 0\n",
    "for line in data:\n",
    "    if line != data[2]:\n",
    "        count_1 += right_order(eval(line), [[2]])\n",
    "        count_2 += right_order(eval(line), [[6]])\n",
    "\n",
    "(count_1+1) * (count_2+2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "005ec0cc-d8bd-4673-b24b-1af999fdd24e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57cf0f90-ea17-4ca5-a2ec-9290c7e099ac",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
