"""Build the Monday, November 16 class deck from the main pull-requests deck (same style, script and captures)."""
import re, sys
from pathlib import Path
main = Path(sys.argv[1]); out = Path(sys.argv[2])
t = main.read_text(encoding="utf-8")
style = re.search(r"<style>.*?</style>", t, re.S).group(0)
script = re.search(r"<script>.*?</script>", t, re.S).group(0)
secs = re.findall(r"<section>.*?</section>", t, re.S)
def sec(title, sub=None):
    s = [x for x in secs if f"<h1>{title}</h1>" in x]
    assert len(s) == 1, title
    s = s[0]
    if sub is not None:
        s = re.sub(r"(<h1>[^<]*</h1>)<p>[^<]*</p>", r"\1<p>" + sub + "</p>", s, count=1)
    return s
L = lambda url, text=None: f'<a href="https://{url}" target="_blank" rel="noopener">{text or url}</a>'
PR = "github.com/GEAP-103/word-practice-app/pull/2"
DECK = "brettrey.github.io/geap-103/materials/pull-requests-projector.html"
new = []
new.append(f'''<section>
  <header><h1>Good morning</h1><p>Monday, November 16 · while you arrive</p></header>
  <ol class="steps">
    <li><div>Open your laptop and the GitHub Copilot app. <b>Don't update Copilot in class.</b> It can take a long time.</div></li>
    <li><div>Not in our class group on GitHub yet? Send me your <b>GitHub username</b> now, in a Blackboard message.</div></li>
    <li><div>Got an invitation? Accept it now: <b>{L("github.com/orgs/GEAP-103/invitation")}</b></div></li>
    <li><div>Did the homework? Get it ready to show me: your app on main, or the word you sent.</div></li>
  </ol>
  <p class="check"><b>Need help?</b> Tell me. I'll start conferences right away.</p>
</section>''')
new.append('''<section>
  <header><h1>Five classes left</h1><p>How you get your marks</p></header>
  <div class="body">
    <p class="big">40% of your grade comes from conferences.</p>
    <p class="big">A conference is a short talk with me: you show me your work and explain it.</p>
    <p class="answer">Today we start the class project.</p>
  </div>
</section>''')
new.append(f'''<section>
  <header><h1>Watch: a pull request, start to finish</h1><p>Brett's app, pull request #2</p></header>
  <p class="lead">Someone changed my app and asked me to include the change. Now I'm the owner. Watch what I do.</p>
  <ol class="steps dense">
    <li><div>Open the pull request: <b>{L(PR)}</b></div></li>
    <li><div><b>Read</b> the change: click <span class="btn">Files changed</span>.</div></li>
    <li><div><b>Review</b> it: try it, and say what I think.</div></li>
    <li><div>Read the <b>comment</b> and the <b>reply</b>.</div></li>
    <li><div><b>Merge</b> it: <span class="btn">Merge pull request</span>, then <span class="btn">Confirm merge</span>.</div></li>
    <li><div>Open the app. Is the change there?</div></li>
  </ol>
  <p class="check">I played both people here: the owner and the person who made the change.</p>
</section>''')
new.append(sec("Who does what?", "Pull request #2"))
rd = sec("Read the change", "Pull request #2")
rd = rd.replace('<p>Here, "Chek" is now "Check".</p>', '<p>Here, "Chek" is now "Check".</p><p class="small">Today there are two changes: the spelling, and a bigger button.</p>')
assert "Today there are two changes" in rd
new.append(rd)
new.append(sec("Review the change", "Pull request #2"))
new.append(sec("Comment, reply, merge", "Pull request #2"))
new.append(sec("Confirm the merge", "Pull request #2"))
new.append('''<section>
  <header><h1>Merged</h1><p>Pull request #2</p></header>
  <div class="shot">
    <div class="imgs"><img src="pull-requests-captures/pr1-merged.png" alt="A pull request marked Merged."></div>
    <div class="cap"><p>The pull request says <b class="w">Merged</b>. The change is in my app now.</p><p>Open the app. The button says <b>Check answer</b>, and it's bigger.</p></div>
  </div>
</section>''')
new.append(sec("The words", "Say them when you talk about your work"))
new.append(sec("Our class benchmark", "The class project"))
new.append(f'''<section>
  <header><h1>An example event: Taboo League</h1><p>{L("github.com/GEAP-103/taboo-league")}</p></header>
  <ol class="steps dense">
    <li><div><b>The question:</b> which two free AIs make the best team at Taboo?</div></li>
    <li><div><b>The contestants:</b> two free chat AIs. One gives a one-word clue (the describer). The other guesses (the guesser). Copilot never competes.</div></li>
    <li><div><b>The rules:</b> each card has a word and some forbidden words. The describer can't use the word, part of it, or a forbidden word.</div></li>
    <li><div><b>The scoring:</b> one point for each right guess. Ten cards, so the top score is 10.</div></li>
    <li><div><b>Too easy?</b> If every team gets 10, the owner makes the cards harder.</div></li>
  </ol>
  <p class="check">Your event can be any game or test for AIs. You write the rules and the scoring <b>before</b> an AI plays.</p>
</section>''')
new.append(f'''<section>
  <header><h1>Now you</h1><p>Two ways to start</p></header>
  <div class="roles">
    <div class="repo you">
      <h2>In our class group</h2>
      <p class="tag">github.com/GEAP-103 shows event-template.</p>
      <ul>
        <li>Do <b>Step 2</b>: make your event (next slide).</li>
        <li>Finished? Do <b>Step 3</b>.</li>
      </ul>
    </div>
    <div class="repo">
      <h2>Not in it yet</h2>
      <p class="tag">Send your username, or accept your invitation.</p>
      <ul>
        <li>Do <b>Step 1</b>: {L(DECK + "#2", "slides 2 to 4")}.</li>
        <li>Plan your event <b>on paper</b>: the question, the rules, the scoring.</li>
      </ul>
    </div>
  </div>
  <p class="after">I'll call you for a conference. Bring what you have.</p>
</section>''')
new.append(sec("Step 2: Make your event", "Your own repository in GEAP-103"))
s3 = sec("Step 3: Add your event to the class benchmark", "A pull request to Brett")
s3 = s3.replace("<b>Don't wait.</b> Start Step 4.", "<b>Then:</b> help a classmate with Step 2.")
assert "help a classmate" in s3
new.append(s3)
new.append('''<section>
  <header><h1>Your conference today</h1><p>Show me, and tell me</p></header>
  <ol class="qs">
    <li><div>Show me your app on main. What was on the other branch?</div></li>
    <li><div>What does your event test? Why can't the AI just know the answer?</div></li>
    <li><div>How will you score it? What makes a good answer?</div></li>
    <li><div>What went wrong today? What did you try?</div></li>
  </ol>
</section>''')
new.append(f'''<section>
  <header><h1>Homework for November 23</h1><p>Before next Monday</p></header>
  <ol class="steps">
    <li><div>Finish <b>Step 2</b>: your event in its own repository in GEAP-103. Run it once yourself.</div></li>
    <li><div>Do <b>Step 3</b>: add your event to the class benchmark with a pull request to me.</div></li>
    <li><div>Haven't sent me a word yet? It's on {L(DECK + "#5", "slides 5 to 8")} of the homework slides.</div></li>
    <li><div>Not in our class group yet? Send me your GitHub username <b>today</b>.</div></li>
  </ol>
  <p class="check">All the steps: <b>{L(DECK)}</b></p>
</section>''')
head = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>GEAP 103: Monday, November 16</title>\n' + style + "\n</head>\n<body>\n\n"
out.write_text(head + "\n\n".join(new) + "\n\n" + script + "\n</body>\n</html>\n", encoding="utf-8")
print(len(new), "slides written to", out.name)
