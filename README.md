<h1 align="center">Key Value Data Store</h1>
<h3>Requirements: </h3>
<ul>
<li>
<h4>Python 3.8</h4>
</li>
<li>
<h4>Python Editor(Spyder,VSC)</h4>
</li>
</ul>
<h3>Modules: </h3>
<ul>
<li>
<h4>os(finding the path of the file)</h4>
</li>
<li>
<h4>json(convert python into json and vice-versa)</h4>
</li>
 <li>
<h4>sys(finding the size of the object)</h4>
</li>
 <li>
<h4>threading(create a thread)</h4>
</li>
  <li>
<h4>time(time to live)</h4>
</li>
</ul>
<h3>Methods: </h3>
<ol>
<li>
<h4>insert()</h4>
  <ul>
    <li>Create a file and insert json data</li>
    <li>Append on an existing file</li>
    <li>Prevent from duplication</li>
  </ul>
</li>
  <li>
<h4>read()</h4>
  <ul>
    <li>Check's files existance</li>
    <li>Display as json object</li>
  </ul>
</li>
 <li>
<h4>read()</h4>
  <ul>
    <li>Check's files existance</li>
    <li>Delete's json object in file</li>
  </ul>
</li>
 <li>
<h4>ttlfunc()</h4>
  <ul>
    <li>Synchronization</li>
    <li>Thread Safety</li>
  </ul>
</li>
</ol>
<h3>Testing: </h3>
<pre><code class="python">
<h4>Unit test methods</h4>
 def test1(self):
        self.assertTrue(insert())
    def test2(self):
        self.assertEqual(read('3rdyear.json','17CS134') ,True )
    def test3(self):
        self.assertEqual(delete('3rdyear.json','17CS237') ,'Key has been deleted' )
    def test4(self):
        self.assertTrue(objsize(1000))
</code></pre>
