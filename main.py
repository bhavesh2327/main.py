{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO1Ktglbx99k0BA2QbysbK1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bhavesh2327/main.py/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "APT7dDjTFaZ2"
      },
      "outputs": [],
      "source": [
        "def main():\n",
        "    import sys\n",
        "\n",
        "    def read_input(lines, idx):\n",
        "        if idx >= len(lines):\n",
        "            return None, idx\n",
        "        N = lines[idx].strip()\n",
        "        if not N.isdigit():\n",
        "            return None, idx\n",
        "        N = int(N)\n",
        "        idx += 1\n",
        "        cases = []\n",
        "        for _ in range(N):\n",
        "            if idx >= len(lines):\n",
        "                return None, idx\n",
        "            X_line = lines[idx].strip()\n",
        "            if not X_line.isdigit():\n",
        "                cases.append((-1, []))\n",
        "                idx += 1\n",
        "                continue\n",
        "            X = int(X_line)\n",
        "            idx += 1\n",
        "            if idx >= len(lines):\n",
        "                cases.append((-1, []))\n",
        "                continue\n",
        "            Yn_line = lines[idx].strip()\n",
        "            if Yn_line == \"\":\n",
        "                cases.append((-1, []))\n",
        "                idx += 1\n",
        "                continue\n",
        "            Yn_split = Yn_line.split()\n",
        "            try:\n",
        "                Yn = list(map(int, Yn_split))\n",
        "            except Exception:\n",
        "                cases.append((-1, []))\n",
        "                idx += 1\n",
        "                continue\n",
        "            if len(Yn) != X:\n",
        "                cases.append((-1, []))\n",
        "            else:\n",
        "                cases.append((X, Yn))\n",
        "            idx += 1\n",
        "        return cases, idx\n",
        "\n",
        "    def process_case(case):\n",
        "        X, Yn = case\n",
        "        if X == -1:\n",
        "            return -1\n",
        "        def rec(idx, acc):\n",
        "            if idx >= len(Yn):\n",
        "                return acc\n",
        "            y = Yn[idx]\n",
        "            if y > 0:\n",
        "                return rec(idx + 1, acc)\n",
        "            return rec(idx + 1, acc + y ** 4)\n",
        "        return rec(0, 0)\n",
        "\n",
        "    # Reading all inputs\n",
        "    lines = []\n",
        "    for line in sys.stdin:\n",
        "        lines.append(line)\n",
        "    cases, _ = read_input(lines, 0)\n",
        "    if cases is None:\n",
        "        return\n",
        "    def print_rec(idx):\n",
        "        if idx >= len(cases):\n",
        "            return\n",
        "        print(process_case(cases[idx]))\n",
        "        print_rec(idx + 1)\n",
        "    print_rec(0)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ]
    }
  ]
}