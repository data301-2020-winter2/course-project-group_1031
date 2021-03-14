{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(path):\n",
    "\n",
    "    data=(pd.read_csv(path)\n",
    "          .dropna()\n",
    "          .rename(columns={'fixed acidity':'F_acidity',\n",
    "                           'volatile acidity':'V_acidity',\n",
    "                           'free sulfur dioxide':'Free_SO2',\n",
    "                           'total sulfur dioxide':'Total_SO2'})\n",
    "          .sort_values(\"quality\", ascending=False)\n",
    "          .reset_index(drop=True)\n",
    "         )\n",
    "    \n",
    "    data.to_csv('../data/processed/austin_data.csv')\n",
    "    \n",
    "    return data\n",
    "                    \n",
    "   "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
