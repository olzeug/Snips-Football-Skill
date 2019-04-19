# Snips-Football-Skill
Mit diesem Skill lernt Snips Fußball kennen.
<h2><a id="user-content-installation" class="anchor" aria-hidden="true" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h2>
<p><strong>Important:</strong> The following instructions assume that <a href="https://snips.gitbook.io/documentation/snips-basics" rel="nofollow">Snips</a> is
already configured and running on your device. <a href="https://snips.gitbook.io/getting-started/installation" rel="nofollow">SAM</a> should
also already be set up and connected to your device and your account.</p>
<ol>
<li>
<p>In the German <a href="https://console.snips.ai/" rel="nofollow">skill store</a> add the
skill <code>Fußball</code> (by olzeug; <a href="https://console.snips.ai/store/de/skill_xvonQMagBvb" rel="nofollow">this</a>) to
your <em>German</em> assistant.</p>
</li>
<li>
<p>Go to the <a href="https://www.football-data.org" rel="nofollow">Football-data</a> website and create
a <a href="https://www.football-data.org/client/register" rel="nofollow">new account</a>,
or <a href="https://www.football-data.org/client/login" rel="nofollow">sign in</a> if you already have one.</p>
</li>
<li>
<p>In the console execute the following command:</p>
<div class="highlight highlight-source-shell"><pre>sam install assistant</pre></div>
<p>You will be asked to enter one value:</p>
<ul>
<li><code>api_key</code>
Here you (copy and) paste the key you generated before.</li>
</ul>
<p>This data is stored on your device.</p>
</li>
<li>
<p>To update the values simply run</p>
<div class="highlight highlight-source-shell"><pre>sam install skills</pre></div>
</li>
<li>
<p>You must have a league file in the directory (/var/lib/snips/dateien/Datenbanken/ligen) which you fill with a small Python program(like <a href="https://github.com/olzeug/Snips-Football-Skill/blob/master/test_write.py">this</a>)(Football-data.org Api: "/v2/competitions/{id}/teams").
<br>   It is important that the folder and files belong to the owner and group "_snips_skills". 
<br>You can change the rights with the following command.</p>
  <div class="highlight highlight-source-shell"><pre>sudo chmod -R _snips_skills:_snips_skills /var/lib/snips/dateien/Datenbanken/ligen/</pre></div>
      </li>
</ol>
<h2><a id="user-content-usage" class="anchor" aria-hidden="true" href="#usage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Usage</h2>
<p>At the moment you can ask for the last game and the next game.</p>
<h3><a id="user-content-example-sentences" class="anchor" aria-hidden="true" href="#example-sentences"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Example sentences</h3>
<ul>
<li><em>Wie hat Paris gespielt?</em></li>
<li><em>Wann spielt Bayern?</em></li>
<li><em>Spielt Real morgen?</em></li>
<li><em>Hat Dortmund gewonnen?</em></li>
</ul>
<h2><a id="user-content-todo" class="anchor" aria-hidden="true" href="#todo"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Todo</h2>
</ul>
<li><em>current Table space</em></li>
<ul>
</article>
      </div>
  </div>



  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>
  </div>
  

  </div>
