#!/usr/bin/env python3 
# -*- coding: utf-8 -*-"
"""
Goldbach - 2017/2020 - by psy (epsylon@riseup.net)

You should have received a copy of the GNU General Public License along
with Goldbach; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import os, sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams.update({'figure.max_open_warning': 0})

class Goldbach(object):
    def __init__(self):
        self.l="love"
        self.dimX=[]
        self.dimY=[]

    def banner(self):
        print("  ____       _     _ _                _     ")
        print(" / ___| ___ | | __| | |__   __ _  ___| |__  ")
        print("| |  _ / _ \| |/ _` | '_ \ / _` |/ __| '_ \ ")
        print("| |_| | (_) | | (_| | |_) | (_| | (__| | | |")
        print(" \____|\___/|_|\__,_|_.__/ \__,_|\___|_| |_|")                                      
        print("\n", 75*"=")
        print(" 'Every even integer greater than 2 can")
        print("  be expressed as the sum of two odd primes'")
        print(75*"=","\n")

    def is_prime(self, n):
        for i in range(3, n):
            if n % i == 0:
                return False
        return True

    def is_odd(self, n):
        if int(n) & 1:
            return True
        return False

    def is_valid_root(self, r):
        import random # generate pseudo-random number
        while True:
            n=(random.randint(4,100))
            r=self.is_odd(n)
            if r is False:
                break
        return n

    def threads(self, n):
        while True:
            n=n-1
            ion = self.is_odd(n)
            if ion is True:
                ipn = self.is_prime(n)
                if ipn is True:
                    self.dimX.append(int(n))
                    if n == 1:
                        break
                else:
                    pass
            else:
                pass

    def generate_graph(self):
        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
            print("\n[Info] Generating 'plots' for number:", self.root)
        if not os.path.exists("graphs/"):
            os.mkdir("graphs/")
        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
            print("\n   + Thread(s):", len(self.tree))
            print('     - Tree =', self.tree)
        plt.figure()
        fig = plt.figure(1)
        ax = plt.gca(projection="3d")
        xs = []
        ys = []
        zs = []
        for t in self.tree:
            z = float(t.rsplit('=',1)[0])
            l = t.rsplit("+",2)[0]
            x = float(l.rsplit("=",1)[1])
            y = float(t.rsplit('+',1)[1])
            xs.append(x)
            ys.append(y)
            zs.append(z)
        ax.scatter(xs,ys,zs, c='red',s=100)
        ax.plot(xs,ys,zs, color='green')
        header = '"Tree" for number '+str(self.root)
        plt.title(header)
        plt.ylabel('Number(s)')
        plt.xlabel('Thread(s)')
        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
            plt.show()
        g = "graphs/"+self.root
        if not os.path.exists(g):
            os.mkdir(g)
            f = open(g+"/"+self.root+"-Goldbach_tree.txt", 'wb')
            fig.savefig(g+"/"+self.root+"-Goldbach_graph.png")
            for t in self.tree:
                f.write(t.encode('utf-8'))
            f.close
            if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                print("\n[Info] Generated 'tree' secuence at folder: "+g+"/\n")
        else:
            if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                print("\n[Info] You have this 'tree' secuence previously saved...\n")
        ax.clear()
        plt.clf()
        print(75*"=", "\n")

    def generate_forest(self, rng):
        print("\n[Info] Generating 'forest' until range:", rng, "\n")
        rng=int(rng)
        for i in range(rng):
            i=i+1
            if i > 2:
                t = self.is_odd(i)
                if t is False:
                   n = i
                   self.root = str(n)
                   print("[Info] Generating 'tree' for number:", self.root)
                   self.generate_tree(n)

    def generate_tree(self, n):
        s=0 # seed counter
        t=0 # threads counter
        x=0 # x counter
        y=0 # y counter
        w=False # warning flag
        self.tree = []
        try:
            if int(n) & 1: 
                print("\n[Error] Number should be always an even. Aborting...\n")
                return
            else:
                if int(n) <= 2:
                    print("\n[Error] Number should be always an integer > 2. Aborting...\n")
                    return
                else:
                    self.threads(n)
                    if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                        print("\n[Info] Prime numbers detected on serie:", len(self.dimX))
                    self.dimY = self.dimX
                    if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                        print("\n[Info] Calculating all possible permutations...\n")
                    for p in self.dimX:
                        for d in self.dimY:
                            t = t + 1
                            r = p + d
                            if r == n:
                                if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                                    print(" Thread:" +str(t) , "->",  p, "+", d, "=", r, "-> FOUND!")
                                l = str(r)+ " = " + str(p)+" + "+str(d)
                                if l not in self.tree:
                                    self.tree.append(l)
                            else:
                                if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                                    print(" Thread:" + str(t), "->",  p, "+", d, "=", r, "-> DISCARDED...")
        except:
            print("\n[Error] Number should be always an integer > 2. Aborting...\n")
            return
        print("\n[Info] Combinations found:", str(len(self.tree)), "\n")
        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
            for t in self.tree:
                print("  ", t)
            graph=input("\nWanna generate a 'graph'? (Y/n)")
            if graph == "n" or graph == "N":
                print("")
                return
            else:
                self.generate_graph()
        else:
            self.generate_graph()

    def run(self, opts=None):
        self.banner()
        self.mode=input("Set mode: single random (default), manual, learning (S/m/l): ") 
        print(40*"-")
        if self.mode == "m" or self.mode == "M" or self.mode == "Manual" or self.mode == "manual": #mode manual
            n=input("Set a number: ")
            try:
               n = int(n)
            except:
                print("\n[Error] Number should be always an even INTEGER greater than 2. Aborting...\n")
                sys.exit(2)
        elif self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn": #mode learning
            rng=input("Set max range (ex: 100 or 9000000) (PRESS ENTER = 100) (STOP = CTRL+z): ")
            if not rng:
                rng=100
        else: # mode single random
            r=input("Set max range (ex: 100 or 9000000) (PRESS ENTER = 100): ")
            if not r:
                r=100
            n = int(self.is_valid_root(r))
        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
            self.root = str(n)
            print("[Info] Generating 'tree' for number:", self.root)
            self.generate_tree(n)
        else:
            try:
               rng = int(rng)
            except:
                print("\n[Error] Max range should be always an even INTEGER greater than 2. Aborting...\n")
                sys.exit(2)
            if not int(rng) > 2:
                print("\n[Error] Max range should be always an even integer GREATER THAN 2. Aborting...\n")
                sys.exit(2)
            else:
                t = self.is_odd(rng)
                if t is True:
                    print("\n[Error] Max range should be always an EVEN integer greater than 2. Aborting...\n")
                    sys.exit(2)
                else:
                    self.generate_forest(rng)
                    print("[Info] 'Forest' correctly generated. Exiting...\n")

if __name__ == "__main__":
    app = Goldbach()
    app.run()
