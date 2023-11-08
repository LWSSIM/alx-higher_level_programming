<h2 id="x04-python-more_data_structures">0x04-python-more_data_structures</h2>
<h1 id="sets">Sets</h1>
<h2 id="what-are-sets-and-how-to-use-them">What are sets and how to use them</h2>
<p>A set is a collection of unique elements, which means that no two elements in a set can be the same. You can create a set in Python using curly braces <code>{}</code> or the <code>set()</code> constructor. Sets are typically used for tasks where uniqueness of elements is important.</p>
<p>Example of creating a set:</p>
<pre class=" language-python"><code class="prism  language-python">my_set <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">}</span>
</code></pre>
<h2 id="what-are-the-most-common-methods-of-set-and-how-to-use-them">What are the most common methods of set and how to use them</h2>
<p>Common methods for sets include:</p>
<ul>
<li><code>add(element)</code>: Adds an element to the set.</li>
<li><code>remove(element)</code>: Removes an element from the set. Raises an error if the element is not found.</li>
<li><code>discard(element)</code>: Removes an element from the set if it exists, without raising an error if not found.</li>
<li><code>union(other_set)</code>: Returns a new set containing all unique elements from both sets.</li>
<li><code>intersection(other_set)</code>: Returns a new set containing elements that are common to both sets.</li>
<li><code>difference(other_set)</code>: Returns a new set with elements from the first set that are not in the second set.</li>
<li><code>issubset(other_set)</code>: Checks if one set is a subset of another.</li>
<li><code>issuperset(other_set)</code>: Checks if one set is a superset of another.</li>
</ul>
<p>Example of using common set methods:</p>
<pre class=" language-python"><code class="prism  language-python">my_set <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">}</span>
my_set<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token number">4</span><span class="token punctuation">)</span>
my_set<span class="token punctuation">.</span>remove<span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span>
other_set <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">}</span>
intersection_set <span class="token operator">=</span> my_set<span class="token punctuation">.</span>intersection<span class="token punctuation">(</span>other_set<span class="token punctuation">)</span>
</code></pre>
<h2 id="when-to-use-sets-versus-lists">When to use sets versus lists</h2>
<p>Use sets when you need to work with a collection of unique elements, and the order of elements doesn’t matter. Lists allow duplicate elements and preserve the order, while sets do not.</p>
<h1 id="dictionaries">Dictionaries</h1>
<h2 id="what-are-dictionaries-and-how-to-use-them">What are dictionaries and how to use them</h2>
<p>A dictionary is a data structure in Python that stores key-value pairs. Each key is unique, and you can access values by their keys. Dictionaries are useful for mapping relationships between objects.</p>
<p>Example of creating a dictionary:</p>
<pre class=" language-python"><code class="prism  language-python">my_dict <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token string">"name"</span><span class="token punctuation">:</span> <span class="token string">"John"</span><span class="token punctuation">,</span> <span class="token string">"age"</span><span class="token punctuation">:</span> <span class="token number">30</span><span class="token punctuation">,</span> <span class="token string">"city"</span><span class="token punctuation">:</span> <span class="token string">"New York"</span><span class="token punctuation">}</span>
</code></pre>
<h2 id="when-to-use-dictionaries-versus-lists-or-sets">When to use dictionaries versus lists or sets</h2>
<p>Use dictionaries when you need to associate values with unique keys. Lists are used for ordered collections of elements, while sets are used for collections of unique elements without key-value associations.</p>
<h2 id="what-is-a-key-in-a-dictionary">What is a key in a dictionary</h2>
<p>A key in a dictionary is a unique identifier used to access and retrieve values associated with that key. Keys are typically strings, numbers, or other immutable objects.</p>
<h2 id="how-to-iterate-over-a-dictionary">How to iterate over a dictionary</h2>
<p>You can iterate over a dictionary using a <code>for</code> loop to access its keys and values.</p>
<p>Example of iterating over a dictionary:</p>
<pre class=" language-python"><code class="prism  language-python">my_dict <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token string">"name"</span><span class="token punctuation">:</span> <span class="token string">"John"</span><span class="token punctuation">,</span> <span class="token string">"age"</span><span class="token punctuation">:</span> <span class="token number">30</span><span class="token punctuation">,</span> <span class="token string">"city"</span><span class="token punctuation">:</span> <span class="token string">"New York"</span><span class="token punctuation">}</span>
<span class="token keyword">for</span> key<span class="token punctuation">,</span> value <span class="token keyword">in</span> my_dict<span class="token punctuation">.</span>items<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>f<span class="token string">"Key: {key}, Value: {value}"</span><span class="token punctuation">)</span>
</code></pre>
<h1 id="lambda-functions">Lambda Functions</h1>
<h2 id="what-is-a-lambda-function">What is a lambda function</h2>
<p>A lambda function is an anonymous, small, and inline function in Python. It is defined using the <code>lambda</code> keyword and is often used for simple operations or as arguments to higher-order functions like <code>map</code>, <code>filter</code>, and <code>reduce</code>.</p>
<p>Example of a lambda function:</p>
<pre class=" language-python"><code class="prism  language-python">square <span class="token operator">=</span> <span class="token keyword">lambda</span> x<span class="token punctuation">:</span> x<span class="token operator">**</span><span class="token number">2</span>
</code></pre>
<h2 id="what-are-the-map-reduce-and-filter-functions">What are the map, reduce, and filter functions</h2>
<ul>
<li>
<p><code>map</code>: The <code>map</code> function applies a given function to each element of an iterable and returns a new iterable containing the results.</p>
<pre class=" language-python"><code class="prism  language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>
squared <span class="token operator">=</span> <span class="token builtin">map</span><span class="token punctuation">(</span><span class="token keyword">lambda</span> x<span class="token punctuation">:</span> x<span class="token operator">**</span><span class="token number">2</span><span class="token punctuation">,</span> numbers<span class="token punctuation">)</span>
</code></pre>
</li>
<li>
<p><code>filter</code>: The <code>filter</code> function filters elements from an iterable based on a given function and returns a new iterable containing only the elements for which the function returns <code>True</code>.</p>
<pre class=" language-python"><code class="prism  language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>
even_numbers <span class="token operator">=</span> <span class="token builtin">filter</span><span class="token punctuation">(</span><span class="token keyword">lambda</span> x<span class="token punctuation">:</span> x <span class="token operator">%</span> <span class="token number">2</span> <span class="token operator">==</span> <span class="token number">0</span><span class="token punctuation">,</span> numbers<span class="token punctuation">)</span>
</code></pre>
</li>
<li>
<p><code>reduce</code>: The <code>reduce</code> function (in Python 3, it’s in the <code>functools</code> module) applies a binary function cumulatively to the elements of an iterable to reduce it to a single value.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">from</span> functools <span class="token keyword">import</span> <span class="token builtin">reduce</span>
numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>
product <span class="token operator">=</span> <span class="token builtin">reduce</span><span class="token punctuation">(</span><span class="token keyword">lambda</span> x<span class="token punctuation">,</span> y<span class="token punctuation">:</span> x <span class="token operator">*</span> y<span class="token punctuation">,</span> numbers<span class="token punctuation">)</span>
</code></pre>
</li>
</ul>
<p>These functions are useful for performing operations on collections of data in a concise and readable way.</p>
