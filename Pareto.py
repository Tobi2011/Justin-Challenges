{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-66-a8c38ec85476>, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-66-a8c38ec85476>\"\u001b[1;36m, line \u001b[1;32m5\u001b[0m\n\u001b[1;33m    alpha = int(input('Provide an Alpha: ')) #is a positive parameter which determines the concentration of data towards the mode\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#Pareto Distribution\n",
    "import matplotlib.pyplot as plt\n",
    "print(' Alpha is a positive parameter which determines\\n\\\n",
    "the concentration of data towards the mode)'\n",
    "alpha = int(input('Provide an Alpha: ')) #is a positive parameter which determines the concentration of data towards the mode\n",
    "print('x_m is the minimum possible value of X')\n",
    "x_m = int(input('Prive a minimum X: ')) #is the minimum possible value of X\n",
    "print ('x is a random variable (x>x_m)\\n\\\n",
    "pick the lower an upper bounds')\n",
    "x_lower = int(input('Lower bound: '))\n",
    "x_higher = int(input('Upper bound: '))\n",
    "pareto = alpha * (x_m ** alpha)/(x_lower ** (alpha+1))\n",
    "variance = ((x_m**2)*alpha)/((alpha-1)**2)/(alpha-2)\n",
    "cdf += 1-(x_m/x_lower)**alpha\n",
    "\n",
    "while x_lower < 4000:\n",
    "    pareto += alpha * (x_m ** alpha)/(x_lower ** (alpha+1))\n",
    "    x_lower += 1\n",
    "\n",
    "\n",
    "    \n",
    "print(f'Probability = {pareto}')\n",
    "print(f'Cumulative density = {cdf}')\n",
    "print(f'Variance = {variance}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_axis = []\n",
    "x_axis = []\n",
    "x = x_m\n",
    "x_high = 10000\n",
    "while x < x_high:\n",
    "    pareto += alpha * (x_m ** alpha)/(x ** (alpha+1))\n",
    "    x += 1\n",
    "    x_axis.append(x)\n",
    "    y_axis.append(alpha * (x_m ** alpha)/(x ** (alpha+1)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "pareto_plot = plt.plot(x_axis,y_axis)\n",
    "plt.xlim([x_m,x_high/2])\n",
    "plt.ylim([0,y_axis[0]])\n",
    "plt.show()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:pythonData]",
   "language": "python",
   "name": "conda-env-pythonData-py"
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
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
