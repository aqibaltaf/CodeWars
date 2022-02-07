<h2><a href="https://www.codewars.com/kata/5412509bd436bd33920011bc">Credit Card Mask</a></h2>

<pre>Usually when you buy something,you're asked whether your credit Card#, phone# or answer to your most secret Q's is still correct.
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.</pre>

<h2>Examples:</h2>
<pre>maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""
&nbsp

<Strong>"What was the name of your first pet?"</Strong>
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"</pre>
