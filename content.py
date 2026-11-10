"""
All page content for the Ben Walder Healing Arts concept redesign.
Every page leads with the visitor's problem, then the method, then a clear next step.
"""
from build import (ARROW, buttons, checklist, cta_final, faq_block, icon, page_hero, ph, photo,
                   section_head, testimonial)

PAGES = []


def add(path, title, description, body, faqs=None, crumb=None, schema=None):
    PAGES.append({"path": path, "title": title, "description": description, "body": body,
                  "faqs": faqs or [], "crumb": crumb or title, "schema": schema or []})


# ==========================================================================
# Shared data
# ==========================================================================
CONDITIONS = [
    {
        "slug": "chronic-back-neck-pain", "icon": "back",
        "tile": "Chronic back, neck or hip pain",
        "tile_text": "Better for a day after massage, then it's back.",
        "title": "Chronic Back & Neck Pain Relief in North County San Diego",
        "desc": "Back, neck or hip pain that keeps returning after PT, massage or chiropractic? Ben uses Structural Integration and manual therapy to work with the whole pattern behind it.",
        "h1": "Back and neck pain that keeps coming back, even after PT.",
        "lede": "If the relief never lasts, the problem usually isn't only where it hurts. Ben looks at how your whole body has organized itself around the pain, and works with that pattern hands-on.",
        "checks": [
            "You feel better for a day or two after massage or an adjustment, then it returns.",
            "The pain moves around: low back one month, neck and shoulders the next.",
            "You've been told the scans look &ldquo;fine,&rdquo; but you're not fine.",
            "You've done the PT exercises and they helped, but only so much.",
            "Sitting, driving or sleeping in certain positions sets it off.",
            "You've started organizing your life around protecting your back.",
        ],
        "why": [
            "Pain that keeps returning is often a sign of compensation. Your body is very good at protecting a sore area by shifting load somewhere else: a slightly rotated pelvis, a ribcage that stopped moving, a neck that took over the work.",
            "Treating only the painful spot relieves it for a while. But the surrounding pattern pulls it straight back. That's why the relief doesn't last.",
            "Ben's work is aimed at the pattern: freeing the fascia and joints that are holding the compensation in place, so the painful area doesn't have to keep working overtime.",
        ],
        "approaches": [("Structural Integration", "/approaches/structural-integration/", "Reorganizes the fascia that holds your posture and compensations in place."),
                       ("Visceral &amp; neural work", "/approaches/visceral-neural-manipulation/", "Releases deeper restrictions around the ribs, abdomen and nerves that often feed back and neck pain."),
                       ("Movement &amp; breath", "/approaches/movement-breath/", "Helps you notice and change the habits that keep loading the same spot.")],
        "expect": ("Many people notice a change in how they stand, breathe or move within the first few sessions.",
                   "Longstanding back and neck patterns usually respond best to a short series or the full Ten-Series."),
        "quote": ("20 years of back pain", "I'd tried everything for my back. Ben was the first person who looked at the whole picture instead of just the spot that hurt."),
        "faqs": [
            ("Can bodywork help back pain when physical therapy didn't?", "<p>It often complements it. PT strengthens and retrains; Ben's work releases the fascia and joint restrictions that can keep pulling you back into the old pattern. Many clients find the two work better together.</p>"),
            ("Is it safe if I have a disc issue or past back surgery?", "<p>Ben adapts the work to your history and works gently around sensitive areas. Bring any imaging or surgical notes to your first visit, and check with your doctor if you're unsure.</p>"),
            ("How is this different from a deep tissue massage?", "<p>Deep tissue focuses on tight muscles in the area that hurts. Ben works more slowly and specifically, and across the whole body, aiming at the pattern that keeps recreating the tension.</p>"),
        ],
    },
    {
        "slug": "old-injuries-scar-tissue", "icon": "scar",
        "tile": "Old injuries and scar tissue",
        "tile_text": "The injury healed. Your body never really did.",
        "title": "Old Injuries & Scar Tissue Bodywork in North County San Diego",
        "desc": "An old sprain, fracture or surgery that still affects how you move? Ben works with scar tissue and the compensation patterns that formed around it.",
        "h1": "The injury healed years ago. Your body still moves like it hasn't.",
        "lede": "A sprained ankle, a fracture, a knee that was never quite the same, scar tissue from surgery: old injuries leave patterns behind. Ben helps your body let go of the ones it no longer needs.",
        "checks": [
            "An old injury still changes how you walk, run or stand.",
            "You have surgical scars that feel tight, numb or &ldquo;stuck.&rdquo;",
            "A bone healed slightly out of place and the area around it never settled.",
            "You protect one side without thinking about it.",
            "New aches have shown up far from the original injury.",
            "You've been told that this is just how it is now.",
        ],
        "why": [
            "When you're injured, your body guards the area: muscles brace, fascia thickens, and you shift your weight to protect it. That's smart in the short term.",
            "The problem is the guarding often stays long after the tissue has healed. Scar tissue can bind layers that are meant to glide, and the compensation spreads up and down the body.",
            "Ben works with the scar itself and with the pattern around it, so the area can rejoin the rest of the body instead of being worked around.",
        ],
        "approaches": [("Structural Integration", "/approaches/structural-integration/", "Restores glide and balance between the layers around an old injury."),
                       ("Visceral &amp; neural work", "/approaches/visceral-neural-manipulation/", "Gentle work for surgical scars and the deeper tissue they can pull on."),
                       ("Craniosacral therapy", "/approaches/craniosacral-therapy/", "Helps a nervous system that's still on guard to stand down.")],
        "expect": ("Scar tissue often softens and moves more freely over a few sessions.",
                   "Patterns built over many years usually need a series to fully reorganize."),
        "quote": ("A pelvis that healed wrong", "After years of working around an old injury, I can finally feel my body as one piece again."),
        "faqs": [
            ("How old is too old for an injury to respond?", "<p>There's no fixed cutoff. Many of Ben's clients come in with injuries that are decades old. Tissue stays adaptable throughout life, which is why old patterns can still change.</p>"),
            ("Can you work directly on surgical scars?", "<p>Yes, once a scar is fully healed and your surgeon has cleared you. Work on scars is gentle and done at a pace that feels comfortable.</p>"),
            ("Will it hurt to work on an old injury?", "<p>It can feel intense in areas that have been restricted for a long time, but Ben works responsively rather than forcefully, and you're always in control of the pressure.</p>"),
        ],
    },
    {
        "slug": "surgery-accident-recovery", "icon": "recovery",
        "tile": "Recovering from surgery or an accident",
        "tile_text": "Get back to moving well, not just moving.",
        "title": "Post-Surgery & Car Accident Recovery Bodywork in North County San Diego",
        "desc": "Hands-on manual therapy to support recovery after surgery or a car accident. Ben works alongside your medical care to restore comfortable movement.",
        "h1": "Recovering from surgery or an accident, and ready to feel like yourself again.",
        "lede": "Your medical team got you through the event. Ben helps with what comes after: stiffness, guarding, scar tissue and a body that doesn't quite trust itself yet.",
        "checks": [
            "You've been cleared by your doctor but still feel stiff and guarded.",
            "Whiplash or impact left your neck, shoulders or back tight for months.",
            "Your scar area feels tight, numb or pulls when you move.",
            "You're compensating for the injured side without meaning to.",
            "Sleep and stress have been off since the accident or surgery.",
            "You want to do more than just &ldquo;get by.&rdquo;",
        ],
        "why": [
            "Surgery and accidents are a shock to the whole system, not just the injured area. Muscles brace, breathing gets shallow and the nervous system stays on high alert.",
            "Even after the tissue heals, that protective state can linger, along with scar tissue and new movement habits.",
            "Ben's work supports the recovery your medical team started: gentle, specific manual therapy to restore movement and help your body come out of protection mode.",
        ],
        "approaches": [("Visceral &amp; neural work", "/approaches/visceral-neural-manipulation/", "Gentle work for surgical scars and the tissue around them."),
                       ("Craniosacral therapy", "/approaches/craniosacral-therapy/", "Calms a nervous system that's been in protection mode since the event."),
                       ("Structural Integration", "/approaches/structural-integration/", "Rebalances the whole body once you're ready for deeper work.")],
        "expect": ("Early sessions are often gentle and focused on the nervous system and comfort.",
                   "As you recover, the work can become more structural to address lasting compensation."),
        "quote": ("Scar tissue from multiple surgeries", "My scars had been tight for years. Ben was patient, careful and explained everything as he went."),
        "faqs": [
            ("How soon after surgery can I come in?", "<p>Once your surgeon has cleared you for hands-on work and any incisions are fully healed. Ben will ask about your procedure and adapt the session to where you are in recovery.</p>"),
            ("Can this be covered after a car accident?", "<p>Sometimes. Coverage depends on your auto policy or claim. Ben can provide receipts and documentation for you to submit; ask your insurer or attorney what they accept.</p>"),
            ("Does this replace physical therapy?", "<p>No. It works alongside PT and your medical care. Many clients find that hands-on work makes their PT exercises feel easier and more effective.</p>"),
        ],
    },
    {
        "slug": "posture-restricted-movement", "icon": "posture",
        "tile": "Posture and restricted movement",
        "tile_text": "You stand up straight. It just doesn't stay.",
        "title": "Posture & Mobility Bodywork in North County San Diego",
        "desc": "Posture that won't hold and movement that feels stiff or restricted? Structural Integration works with the fascia that shapes how you stand and move.",
        "h1": "Posture that won't hold, and movement that feels harder than it should.",
        "lede": "You can't stretch or will your way into better posture if the tissue holding you there won't let go. Ben works with the structure itself, so better alignment becomes the easy default.",
        "checks": [
            "You correct your posture, and a minute later you're slumped again.",
            "Your shoulders round forward or one sits higher than the other.",
            "Turning your head, reaching overhead or bending down feels limited.",
            "Desk work leaves you stiff and heavy by the afternoon.",
            "Stretching helps for an hour and then it's gone.",
            "You feel older in your body than you are.",
        ],
        "why": [
            "Posture isn't just a habit. It's held in place by fascia, the connective tissue that wraps and links every muscle. Over years of desk work, injuries and stress, it adapts to the shapes you spend the most time in.",
            "That's why trying harder to sit up straight doesn't last: you're fighting the tissue instead of changing it.",
            "Structural Integration works with that tissue directly, layer by layer, so your body can find a more upright, easier way to be without constant effort.",
        ],
        "approaches": [("Structural Integration", "/approaches/structural-integration/", "The core method for lasting change in posture and alignment."),
                       ("Movement &amp; breath", "/approaches/movement-breath/", "Teaches your body to use its new range in daily life."),
                       ("The Ten-Series", "/ten-series/", "A full-body sequence for comprehensive structural change.")],
        "expect": ("People often notice they stand taller and breathe more easily after the first session.",
                   "For lasting change, the Ten-Series is designed exactly for this."),
        "quote": ("Rounded shoulders and stiffness", "I walked out standing taller without trying. Friends asked what I'd changed."),
        "faqs": [
            ("Can bodywork actually change posture?", "<p>Structural Integration is designed for exactly this. By releasing and reorganizing the fascia that holds habitual shapes, it can make a more balanced posture feel natural instead of effortful.</p>"),
            ("Do I need to do exercises at home?", "<p>Ben may suggest a few simple movement or awareness practices, but there's no heavy homework. The goal is to make good posture feel easier, not to add another routine.</p>"),
            ("Is the Ten-Series necessary for posture?", "<p>Not always. Some people get what they need from a few sessions. The Ten-Series is the most complete option if your posture has been a long-term issue.</p>"),
        ],
    },
    {
        "slug": "stress-tension", "icon": "stress",
        "tile": "Stress and tension held in the body",
        "tile_text": "Wired, tired, and you can't switch off.",
        "title": "Bodywork for Stress & Nervous System Tension in North County San Diego",
        "desc": "Tight jaw, shallow breathing, shoulders up by your ears? Gentle craniosacral, visceral and breath work to help your nervous system settle.",
        "h1": "When stress lives in your body and won't let go.",
        "lede": "A clenched jaw, shoulders up by your ears, breath that stops at your chest, a body that can't seem to rest. Ben's gentler work helps your nervous system remember how to settle.",
        "checks": [
            "You clench your jaw or grind your teeth.",
            "Your breathing feels shallow or stuck high in your chest.",
            "Your shoulders and neck are tight no matter what you do.",
            "You feel tired but wired, especially at night.",
            "Massage feels nice but doesn't really reach it.",
            "You feel disconnected from your body.",
        ],
        "why": [
            "Long periods of stress teach the body to stay braced: muscles guard, breathing gets shallow and the nervous system stays switched on. Over time, that becomes the new normal.",
            "Because it's driven by the nervous system, pressing harder on tight muscles rarely changes it for long.",
            "Ben uses slower, subtler approaches that speak to the nervous system directly, alongside breath work, so your body can shift out of protection and into rest.",
        ],
        "approaches": [("Craniosacral therapy", "/approaches/craniosacral-therapy/", "Light, calming work that many people find deeply restorative."),
                       ("Visceral work", "/approaches/visceral-neural-manipulation/", "Frees the diaphragm and abdomen so breathing can drop and deepen."),
                       ("Herbal support", "/herbal-nutrition/", "Herbs, food and sleep habits to support a calmer nervous system.")],
        "expect": ("Many people leave their first session feeling calmer and more settled.",
                   "Regular sessions help the body learn that calm is available, not just a one-off."),
        "quote": ("Stress held in the body", "I left feeling regulated in a way I hadn't in years. It felt more personal than any massage I've had."),
        "faqs": [
            ("Is this therapy for anxiety?", "<p>Ben doesn't treat mental health conditions, and this isn't a replacement for counseling or medical care. Many people find that calming, body-based work helps them feel more settled alongside that support.</p>"),
            ("Is craniosacral work deep or light?", "<p>Light. It uses gentle, still contact rather than deep pressure, which is why many people find it so relaxing.</p>"),
            ("Can herbs help with stress and sleep?", "<p>Ben offers consultations on herbs, food and daily habits that support rest and resilience. It's educational and personalized, and he'll check for anything that might interact with your medications.</p>"),
        ],
    },
    {
        "slug": "athletes", "icon": "athlete",
        "tile": "Athletes, surfers and runners",
        "tile_text": "Move more freely and recover better.",
        "title": "Structural Integration for Athletes, Surfers & Runners in North County San Diego",
        "desc": "Bodywork for athletes, surfers and runners: improve range of motion, movement efficiency and recovery with Structural Integration and manual therapy.",
        "h1": "For athletes, surfers and runners who want to move better, not just push harder.",
        "lede": "Old injuries, one-sided sports and years of training leave patterns that cap your range and efficiency. Ben helps your body move as one connected system again.",
        "checks": [
            "One shoulder or hip is noticeably tighter than the other.",
            "Your paddling, stride or swing feels restricted.",
            "Old injuries keep flaring when training gets heavier.",
            "You stretch and foam-roll constantly and it doesn't hold.",
            "Recovery takes longer than it used to.",
            "You want to keep doing this for decades.",
        ],
        "why": [
            "Most sports are repetitive and often one-sided. Over time, your body builds patterns around that: one side shortens, old injuries get worked around, and range of motion quietly shrinks.",
            "Those patterns cost you efficiency and increase the load on the same tissues, which is why the same injuries keep coming back.",
            "Structural Integration rebalances the whole body so force travels through it more evenly, and you get more out of the same effort.",
        ],
        "approaches": [("Structural Integration", "/approaches/structural-integration/", "Rebalances the whole body for range, efficiency and resilience."),
                       ("The Ten-Series", "/ten-series/", "A full-body reset many athletes do once and maintain afterwards."),
                       ("Movement &amp; breath", "/approaches/movement-breath/", "Carries the change into your sport.")],
        "expect": ("Athletes often notice freer range of motion and easier breathing right away.",
                   "The Ten-Series, done in an off-season, is the most complete reset."),
        "quote": ("Surfer with a stiff shoulder", "My paddling feels smoother and my shoulder isn't the first thing I think about in the water anymore."),
        "faqs": [
            ("Should I come before or after a big event?", "<p>Avoid deep structural work in the few days right before a race or competition. Lighter work beforehand and deeper sessions during recovery or the off-season usually work best.</p>"),
            ("Is this sports massage?", "<p>Not exactly. Sports massage focuses on recovery and tight muscles. Structural Integration aims at the underlying pattern of how your body is organized, for longer-lasting change.</p>"),
            ("How often should athletes come in?", "<p>Many athletes do a series once and then come in for maintenance every few weeks or around training blocks. Ben will help you figure out what fits your season.</p>"),
        ],
    },
]

APPROACHES = [
    {
        "slug": "structural-integration", "icon": "layers", "name": "Structural Integration",
        "title": "Structural Integration (Rolfing) in North County San Diego",
        "desc": "Structural Integration, often called Rolfing, is hands-on work with fascia to improve posture, mobility and comfort over time. Learn how it works and who it helps.",
        "h1": "Structural Integration: working with the tissue that holds your shape.",
        "lede": "Often called Rolfing, Structural Integration treats the body as one connected system. It works with fascia, the connective tissue that links every muscle, to improve posture, mobility, breathing and comfort over time.",
        "short": "The core of Ben's work. Reorganizes the fascia that holds posture and compensation in place.",
        "what": [
            "Fascia is a continuous web of connective tissue that surrounds and links your muscles, bones and organs. It adapts to how you use your body: injuries, habits and stress all leave a mark.",
            "In Structural Integration, Ben uses slow, specific pressure and movement to release and reorganize that web, so your body can find a more balanced, easier way to stand and move.",
            "It's based on the work of Dr. Ida Rolf, and is usually done as a series of sessions that build on each other, though single sessions can help too.",
        ],
        "good_for": ["Chronic back, neck and hip pain", "Posture that won't hold", "Old injuries and compensation", "Restricted movement", "Athletes wanting better efficiency"],
        "feels": "Slower and more specific than massage. Some areas can feel intense, but Ben works responsively, with your feedback, and you're always in control of the pressure. You may be asked to move slowly during the work.",
        "note": "Ben to confirm: if he holds certification from the Dr. Ida Rolf Institute, this page can use the Rolfing® trademark. If not, &ldquo;Structural Integration&rdquo; is the correct term.",
    },
    {
        "slug": "craniosacral-therapy", "icon": "head", "name": "Craniosacral therapy",
        "title": "Craniosacral Therapy in North County San Diego",
        "desc": "Craniosacral therapy is a gentle, light-touch approach that supports the nervous system and eases patterns of stress, guarding and overload.",
        "h1": "Craniosacral therapy: gentle work for a nervous system that won't settle.",
        "lede": "A slower, subtler approach that uses light, still contact to help the nervous system ease out of stress, guarding and overload. Most people find it deeply calming.",
        "short": "Light, calming work for stress, guarding and a nervous system stuck on high alert.",
        "what": [
            "Craniosacral therapy works with the membranes and fluid around the brain and spinal cord, and the bones of the skull, spine and sacrum.",
            "Ben uses very light, patient contact, often at the head, neck, spine or pelvis, to support your body's own ability to release tension and settle.",
            "He often weaves it into structural sessions when the body needs to calm down before deeper work can land.",
        ],
        "good_for": ["Stress and tension held in the body", "Jaw clenching and neck tension", "Recovery after accidents or surgery", "Feeling wired, tired or disconnected", "People sensitive to deep pressure"],
        "feels": "Very gentle. Most people feel warmth, softening or deep relaxation, and some drift toward sleep.",
        "note": "",
    },
    {
        "slug": "visceral-neural-manipulation", "icon": "spiral", "name": "Visceral &amp; neural manipulation",
        "title": "Visceral & Neurovascular Manipulation in North County San Diego",
        "desc": "Gentle manual therapy for the organs, nerves and blood vessels and the tissue around them, which can influence breathing, posture, pain and movement.",
        "h1": "Visceral and neural work: releasing the restrictions you can't stretch.",
        "lede": "Gentle, specific manual work with the organs, nerves and blood vessels, and the connective tissue around them. These deeper restrictions can affect breathing, posture and pain in ways stretching never reaches.",
        "short": "Gentle work with organs, nerves and vessels for deep restrictions, scars and breathing.",
        "what": [
            "Your organs are suspended and connected by fascia too. When that tissue gets restricted, from surgery, injury, illness or long-term tension, it can pull on the ribs, spine and pelvis.",
            "Visceral manipulation uses gentle, precise contact, especially around the abdomen, diaphragm, ribs and pelvis, to restore normal movement there.",
            "Neurovascular manipulation works with nerves and blood vessels, easing compression and guarding so tissue can move and communicate better.",
        ],
        "good_for": ["Surgical and abdominal scars", "Breathing that feels restricted", "Back and neck pain with no clear cause", "Post-accident recovery", "Nerve-related tightness and guarding"],
        "feels": "Gentle and specific. You may feel subtle pulling or softening, sometimes far from where Ben's hands are.",
        "note": "",
    },
    {
        "slug": "movement-breath", "icon": "breath", "name": "Movement &amp; breath",
        "title": "Movement & Breath Education in North County San Diego",
        "desc": "Movement, breathing and body-awareness practices woven into Ben's sessions to help you notice and change the habits behind tension and pain.",
        "h1": "Movement and breath: making the change last outside the session.",
        "lede": "Hands-on work opens new options for your body. Movement and breath practice help you actually use them, so the change carries into how you sit, walk, work and train.",
        "short": "Simple practices that help your body keep its new options in daily life.",
        "what": [
            "Ben weaves movement, breathing and awareness exercises into most sessions. They help you notice the habitual patterns of tension, posture and effort that keep recreating the problem.",
            "This isn't a workout. It's slower, more like learning to feel what your body is doing so you can choose differently.",
            "You'll leave with one or two simple things to try, not a long list of homework.",
        ],
        "good_for": ["Making hands-on results last", "Desk workers and drivers", "Athletes refining movement", "People who hold their breath under stress", "Anyone who wants to understand their body better"],
        "feels": "Easy and exploratory. Comfortable clothing is all you need.",
        "note": "",
    },
]

TEN_SERIES = [
    ("Sleeve", 1, "Breath", "Frees the outer layers around the ribs, shoulders and hips so breathing can open up."),
    ("Sleeve", 2, "Foundation", "Feet and lower legs: building support from the ground up."),
    ("Sleeve", 3, "Side line", "Balances front and back along the sides of the body."),
    ("Core", 4, "Inside line", "Inner legs up to the pelvic floor."),
    ("Core", 5, "Front core", "Abdomen and the deep hip flexors that link legs to spine."),
    ("Core", 6, "Back core", "Back of the legs, sacrum and spine."),
    ("Core", 7, "Head &amp; neck", "Lets the head sit easily on top of the spine."),
    ("Integration", 8, "Lower body", "Integrates the pelvis and legs into the new pattern."),
    ("Integration", 9, "Upper body", "Integrates the shoulders, arms and ribs."),
    ("Integration", 10, "Whole body", "Brings everything together into one coherent, easy way of moving."),
]

FAQS_CORE = [
    ("Who is this work for?", "<p>Anyone who wants individualized, hands-on care for their body. You don't need to be flexible, athletic or know anything about bodywork. People most often come in for chronic pain, old injuries, recovery from surgery or accidents, posture, tension or stress. All ages and backgrounds are welcome.</p>"),
    ("Is this the same as massage?", "<p>Not exactly. It's usually slower and more specific than massage, and it looks at long-term patterns across your whole body rather than just relaxation or temporary relief in one spot.</p>"),
    ("What is Structural Integration?", "<p>Also called Rolfing, it's hands-on bodywork that treats the body as one connected system. It works mainly with fascia, the connective tissue that links everything, to improve posture, mobility, breathing and comfort over time.</p>"),
    ("Is the work painful?", "<p>It can feel intense in areas that have been restricted for a long time, but Ben works responsively rather than forcefully. You're always in control of the pressure, and most people find it manageable and relieving.</p>"),
    ("How many sessions will I need?", "<p>It depends on your goals. Some people feel a meaningful change in a few sessions; others choose ongoing work like the Ten-Series for longstanding patterns. You'll decide together, with no pressure toward a long commitment.</p>"),
    ("How much does it cost?", f"<p>First sessions are {ph('first')} (90 minutes), single sessions are {ph('single')}, and the Ten-Series package is {ph('series')}. See <a href=\"/pricing/\">pricing</a> for every option.</p>"),
    ("Is this covered by insurance?", "<p>Usually not by standard health insurance. Ben can provide receipts and documentation you can submit for possible reimbursement, and HSA/FSA cards are often accepted for this kind of care. Check with your plan.</p>"),
    ("What should I wear?", "<p>Comfortable clothing you can move in. Shorts and a tank top or sports bra work well. Ben may ask you to adjust clothing for access to certain areas, always based on your comfort and preferences.</p>"),
    ("How long is a session?", "<p>First sessions are about 90 minutes, which includes time to talk through your history. Follow-up sessions are usually 60–75 minutes.</p>"),
    ("Can I do this alongside physical therapy or chiropractic?", "<p>Yes, and many clients do. Ben's work often makes other care more effective. He works alongside your medical team, not instead of it.</p>"),
    ("Do you offer herbal consultations online?", "<p>Yes. Herbal and nutritional consultations can be done in person or online, so you don't need to be in San Diego.</p>"),
    ("I'm still not sure this is for me.", "<p>That's completely fine. Skeptics and people who aren't sure what they need are welcome. <a href=\"/contact/#call\">Book a free 15-minute call</a> and talk it through with Ben first.</p>"),
]


# ==========================================================================
# Homepage
# ==========================================================================
def home():
    tiles = "".join(
        f'<li class="tile"><a href="/conditions/{c["slug"]}/">{icon(c["icon"], "tile-icon")}'
        f'<div><h3>{c["tile"]}</h3><p>{c["tile_text"]}</p></div>{ARROW}</a></li>' for c in CONDITIONS)

    why_svg = """
<svg class="why-figure" viewBox="0 0 300 420" fill="none" stroke-linecap="round" stroke-linejoin="round" role="img" aria-labelledby="whyfig-title whyfig-desc">
  <title id="whyfig-title">How an old injury travels</title>
  <desc id="whyfig-desc">A standing figure. A line runs from an old ankle injury, up through the knee, hip and ribs, to a painful shoulder on the other side.</desc>
  <g class="body-outline" stroke-width="1.4">
    <circle cx="150" cy="44" r="24"/>
    <path d="M150 68v14M108 96c14-10 70-10 84 0M108 96l-22 92M192 96l22 92M108 96c-4 50 4 90 10 112M192 96c4 50-4 90-10 112M118 208c10 6 54 6 64 0M122 210l-6 96-4 96M178 210l6 96 4 96M112 402h-18M188 402h18"/>
  </g>
  <path d="M110 396 C120 360 116 330 120 306 C126 270 136 240 146 212 C158 176 168 150 172 128 C176 112 182 104 190 98" stroke="#C9D1BF" stroke-width="2.2" stroke-dasharray="1 7"/>
  <circle cx="110" cy="396" r="8" fill="#C9D1BF"/>
  <circle cx="120" cy="306" r="4" fill="#C9D1BF"/>
  <circle cx="146" cy="212" r="4" fill="#C9D1BF"/>
  <circle cx="172" cy="128" r="4" fill="#C9D1BF"/>
  <circle cx="190" cy="98" r="9" fill="#B5532F"/>
  <g font-family="Inter, sans-serif" font-size="12" fill="#F6F1EA">
    <text x="8" y="400">Old ankle sprain</text>
    <text x="10" y="310">Knee adapts</text>
    <text x="186" y="216">Hip shifts</text>
    <text x="186" y="132">Ribs stiffen</text>
    <text x="206" y="90">Shoulder pain</text>
  </g>
</svg>"""

    series_items = "".join(
        f'<li><span class="dot">{n}</span><span class="phase">{phase}</span><h4>{name}</h4></li>'
        for phase, n, name, _ in TEN_SERIES)

    body = f"""
<div class="thread-wrap">
<section class="hero" id="hero">
  <div class="container hero-grid">
    <div class="hero-copy reveal">
      <span class="eyebrow">Structural Integration &amp; manual therapy · North County San Diego</span>
      <h1>Still in pain after PT, massage, and chiropractic?</h1>
      <p class="lede">Hands-on Structural Integration and manual therapy for chronic pain, old injuries and post-surgical recovery, in {ph("city")}, North County San Diego.</p>
      {buttons()}
      <p class="hero-note">First session 90 min · {ph("first")} · Free 15-minute call if you're not sure</p>
    </div>
    <div class="hero-media" data-thread="0.93" data-thread-y="1">
      {photo("Ben's hands working on a client's upper back. Close, natural light, both relaxed.")}
    </div>
  </div>
</section>

<div class="trust-strip">
  <div class="container">
    <ul class="trust-list" aria-label="Why people trust Ben">
      <li><span class="stars" aria-hidden="true">★★★★★</span><span>{ph("rating")} on Google · {ph("reviews")} reviews</span></li>
      <li>{icon("clock")}<span>15 years of study &amp; practice</span></li>
      <li>{icon("badge")}<span>{ph("cert")}</span></li>
      <li>{icon("pin")}<span>Private studio in {ph("city")}</span></li>
    </ul>
  </div>
</div>

<section class="section" id="what-brings-you-in">
  <div class="container">
    <div data-thread="0.03" data-thread-y="0.1"></div>
    {section_head("What brings you in?", "Start with what's going on for you.", "Pick the one that sounds most like you. Each page explains why it keeps happening and how Ben works with it.")}
    <ul class="tiles reveal">{tiles}</ul>
  </div>
</section>

<section class="section section--forest" id="why">
  <div class="container split split--rev">
    <div class="reveal" data-thread="0.5" data-thread-y="0.5">{why_svg}</div>
    <div class="reveal">
      <span class="eyebrow">Why it keeps coming back</span>
      <h2>The spot that hurts is rarely the whole story.</h2>
      <p class="lede">If the relief from massage, adjustments or stretching never lasts, there's usually a reason.</p>
      <ul class="why-points">
        <li><span class="num">1</span><div>Your body protects an injured or overworked area by shifting load somewhere else. That's smart in the short term.</div></li>
        <li><span class="num">2</span><div>Over months and years, those shifts become your new normal, held in place by fascia, the connective tissue that links everything.</div></li>
        <li><span class="num">3</span><div>Treating only the painful spot gives temporary relief. Ben works with the whole pattern, so the pain has less to come back to.</div></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--linen" id="how-it-works">
  <div class="container">
    <div data-thread="0.97" data-thread-y="0"></div>
    {section_head("How it works", "Three simple steps. No pressure at any of them.", "", center=True)}
    <ol class="steps reveal">
      <li class="step"><div class="step-num">1</div><h3>Talk</h3><p>A free 15-minute call about your history, what you've tried and what you want to get back to.</p><span class="meta">Free · by phone or video</span></li>
      <li class="step"><div class="step-num">2</div><h3>First session</h3><p>Ben assesses how your body is organized, then works hands-on, so you can feel the difference on day one.</p><span class="meta">90 minutes · {ph("first")}</span></li>
      <li class="step"><div class="step-num">3</div><h3>Your plan</h3><p>Single sessions, a short series or the full Ten-Series. You decide together, based on your goals.</p><span class="meta">No long-term contracts</span></li>
    </ol>
  </div>
</section>

<section class="section" id="results">
  <div class="container">
    <div data-thread="0.03" data-thread-y="0"></div>
    {section_head("Results", "People come in after years of trying everything.", "")}
    <div class="testimonial-grid reveal">
      {testimonial("20 years of back pain", "I'd lived with pain for over twenty years. Ben was the first person who looked for the cause instead of chasing the symptom. I finally feel like I'm getting better, not just managing.", feature=True)}
      <div class="stack">
        {testimonial("A pelvis that healed wrong", "He found things through touch that no one had noticed before, and explained them so I understood my own body.")}
        {testimonial("Scar tissue from surgeries", "Warm, attentive and incredibly skilled. My scars move in ways they haven't in years.")}
      </div>
    </div>
    <p class="mt-32"><a class="text-link" href="/results/">Read more client stories {ARROW}</a></p>
  </div>
</section>

<section class="section section--linen" id="ten-series">
  <div class="container">
    <div class="split split--55" style="align-items:end;margin-bottom:48px">
      <div data-thread="0.5" data-thread-y="0">
        <span class="eyebrow">The Ten-Series</span>
        <h2>The deepest work Ben offers: ten sessions, whole body, built to last.</h2>
      </div>
      <div>
        <p class="muted">Based on Dr. Ida Rolf's method. Each session builds on the last, from the breath and outer layers, into the core, and finally integrating it all into a new, easier baseline.</p>
        <p class="mb-0"><strong style="font-family:var(--serif);font-size:28px;font-weight:500">{ph("series")}</strong> <span class="muted small">· prepaid package · payment plans available</span></p>
      </div>
    </div>
    <ol class="series series--horizontal reveal">{series_items}</ol>
    <div class="btn-row mt-48">
      <a class="btn btn-primary" href="/ten-series/">See the Ten-Series</a>
      <a class="btn btn-secondary" href="/contact/#call">Is it right for me? Ask Ben</a>
    </div>
  </div>
</section>

<section class="section" id="meet-ben">
  <div class="container split">
    <div class="reveal" data-thread="0.03" data-thread-y="0.5">{photo("Portrait of Ben in the studio, eye level, half-smile, natural light.")}</div>
    <div class="reveal">
      <span class="eyebrow">Meet Ben</span>
      <h2>I came to this work the same way most of my clients do: in pain.</h2>
      <p>An injury and years of chronic pain sent me looking for answers. What I found changed how I understand the body, and turned into 15 years of study in Structural Integration, manual therapy, Chinese medicine, herbalism and nutrition.</p>
      <p>I don't see sessions as fixing you. I see them as understanding how your body has adapted, and helping it find a better way. Your story and your feedback guide the work.</p>
      <p class="signature">— Ben</p>
      <ul class="badges" aria-label="Training">
        <li>Structural Integration</li><li>Craniosacral</li><li>Visceral manipulation</li><li>Herbalism</li><li>{ph("cert")}</li>
      </ul>
      <a class="text-link" href="/about/">Read Ben's story {ARROW}</a>
    </div>
  </div>
</section>

<section class="section section--linen" id="pricing">
  <div class="container">
    <div data-thread="0.97" data-thread-y="0"></div>
    {section_head("Pricing", "Clear prices. No surprises.", "", center=True)}
    {price_cards()}
    <p class="price-footnote center">HSA/FSA often accepted · Receipts provided for possible reimbursement · <a href="/pricing/">All options &amp; policies</a></p>
  </div>
</section>

<section class="section" id="faq">
  <div class="container split split--55" style="align-items:start">
    <div data-thread="0.03" data-thread-y="0">
      <span class="eyebrow">Questions</span>
      <h2>What people usually ask first.</h2>
      <p class="muted">Still unsure? <a class="text-link" href="/contact/#call">Talk to Ben for 15 minutes, free {ARROW}</a></p>
    </div>
    <div>{faq_block(HOME_FAQS)}<p class="mt-32"><a class="text-link" href="/faq/">See all questions {ARROW}</a></p></div>
  </div>
</section>

{cta_final()}
</div>
"""
    return body


def price_cards():
    return f"""
<div class="price-cards reveal">
  <div class="price-card">
    <h3>First session</h3><div class="duration">90 minutes · assessment + hands-on work</div>
    <div class="price">{ph("first")}</div>
    <ul><li>Full history and movement assessment</li><li>Hands-on session tailored to you</li><li>Honest recommendation for next steps</li></ul>
    <a class="btn btn-secondary" href="/pricing/#book">Book first session</a>
  </div>
  <div class="price-card">
    <h3>Single session</h3><div class="duration">60–75 minutes</div>
    <div class="price">{ph("single")}</div>
    <ul><li>Structural, craniosacral or visceral work, or a mix</li><li>Movement and breath guidance</li><li>Book as needed, no commitment</li></ul>
    <a class="btn btn-secondary" href="/pricing/#book">Book a session</a>
  </div>
  <div class="price-card card--forest">
    <span class="flag">Most complete</span>
    <h3>The Ten-Series</h3><div class="duration">10 sessions · prepaid package</div>
    <div class="price">{ph("series")}</div>
    <ul><li>Full-body, step-by-step reorganization</li><li>Saves {ph("$___")} vs. single sessions</li><li>Payment plan available</li></ul>
    <a class="btn btn-primary" href="/ten-series/">Start the Ten-Series</a>
  </div>
</div>"""


HOME_FAQS = [FAQS_CORE[3], FAQS_CORE[4], FAQS_CORE[1], FAQS_CORE[6], FAQS_CORE[7]]

add("/", "Structural Integration & Manual Therapy for Chronic Pain in North County San Diego | Ben Walder Healing Arts",
    "Still in pain after PT, massage and chiropractic? Ben Walder offers Structural Integration (Rolfing), craniosacral and visceral work for chronic pain, old injuries and recovery in North County San Diego.",
    home(), faqs=HOME_FAQS, crumb="Home")


# ==========================================================================
# Conditions
# ==========================================================================
def condition_page(c):
    approach_cards = "".join(
        f'<a class="card card-link" href="{href}"><h3>{name}</h3><p>{line}</p><span class="text-link">Learn more {ARROW}</span></a>'
        for name, href, line in c["approaches"])
    why = "".join(f"<p>{p}</p>" for p in c["why"])
    chip, quote = c["quote"]
    others = "".join(
        f'<li class="tile"><a href="/conditions/{o["slug"]}/">{icon(o["icon"], "tile-icon")}<div><h3>{o["tile"]}</h3><p>{o["tile_text"]}</p></div>{ARROW}</a></li>'
        for o in CONDITIONS if o["slug"] != c["slug"])[:]
    return f"""
{page_hero("Conditions", c["h1"], c["lede"], crumbs=[("Conditions", "/conditions/"), (c["tile"], None)])}

<section class="section">
  <div class="container">
    {section_head("Does this sound like you?", "If you're nodding along, you're in the right place.")}
    <div class="checklist-card reveal">{checklist(c["checks"])}</div>
  </div>
</section>

<section class="section section--forest">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Why it persists</span>
      <h2>Why it keeps happening.</h2>
      <div class="lede" style="max-width:none">{why}</div>
    </div>
    <div class="reveal">{photo("Ben assessing a client's standing posture, hand lightly on the back.", "forest")}</div>
  </div>
</section>

<section class="section section--linen">
  <div class="container">
    {section_head("How Ben works with it", "The methods, chosen for your situation.", "Every session is tailored. These are the approaches Ben most often uses for this.")}
    <div class="grid grid-3 reveal">{approach_cards}</div>
  </div>
</section>

<section class="section">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">What to expect</span>
      <h2>What usually changes, and when.</h2>
      <p>{c["expect"][0]}</p>
      <p>{c["expect"][1]}</p>
      <p class="muted small">Everyone is different, and Ben will never push you toward more sessions than you need. Progress is checked together as you go.</p>
      {buttons()}
    </div>
    <div class="reveal">{testimonial(chip, quote)}</div>
  </div>
</section>

<section class="section section--linen">
  <div class="container split split--55" style="align-items:start">
    <div><span class="eyebrow">Questions</span><h2>Common questions about this.</h2></div>
    <div>{faq_block(c["faqs"])}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("Something else?", "Other reasons people come in.")}
    <ul class="tiles">{others}</ul>
  </div>
</section>

{cta_final()}
"""


conditions_tiles = "".join(
    f'<li class="tile"><a href="/conditions/{c["slug"]}/">{icon(c["icon"], "tile-icon")}<div><h3>{c["tile"]}</h3><p>{c["tile_text"]}</p></div>{ARROW}</a></li>'
    for c in CONDITIONS)
add("/conditions/", "What Ben Helps With: Chronic Pain, Old Injuries, Recovery & More",
    "Chronic back and neck pain, old injuries and scar tissue, surgery and accident recovery, posture, stress and athletic performance. Find what sounds like you.",
    f"""
{page_hero("Conditions", "What brings you in?", "Start with what's going on for you. Each page explains why it keeps happening, how Ben works with it, and what to expect.", crumbs=[("Conditions", None)], show_buttons=False)}
<section class="section"><div class="container"><ul class="tiles">{conditions_tiles}</ul>
<p class="mt-48 muted">Don't see your situation? <a class="text-link" href="/contact/#call">Ask Ben in a free 15-minute call {ARROW}</a></p></div></section>
{cta_final()}""", crumb="Conditions")

for c in CONDITIONS:
    add(f"/conditions/{c['slug']}/", c["title"], c["desc"], condition_page(c), faqs=c["faqs"], crumb=c["tile"])


# ==========================================================================
# Approaches
# ==========================================================================
def approach_page(a):
    what = "".join(f"<p>{p}</p>" for p in a["what"])
    good = "".join(f"<li>{g}</li>" for g in a["good_for"])
    note = f'<p class="disclaimer">{a["note"]}</p>' if a["note"] else ""
    others = "".join(
        f'<a class="card card-link" href="/approaches/{o["slug"]}/">{icon(o["icon"], "card-icon")}<h3>{o["name"]}</h3><p>{o["short"]}</p></a>'
        for o in APPROACHES if o["slug"] != a["slug"])
    schema = [{"@context": "https://schema.org", "@type": "Service", "name": a["name"].replace("&amp;", "&"),
               "serviceType": a["name"].replace("&amp;", "&"), "description": a["desc"],
               "provider": {"@id": "https://benwalder-redesign.onrender.com/#business"},
               "areaServed": "North County San Diego"}]
    body = f"""
{page_hero("Approaches", a["h1"], a["lede"], crumbs=[("Approaches", "/approaches/"), (a["name"], None)])}
<section class="section">
  <div class="container split" style="align-items:start">
    <div class="prose reveal"><span class="eyebrow">What it is</span><h2 class="mt-0">How it works.</h2>{what}{note}</div>
    <div class="reveal">{photo("Close-up of Ben's hands during a " + a["name"].replace("&amp;", "and").lower() + " session.", "sage")}</div>
  </div>
</section>
<section class="section section--linen">
  <div class="container grid grid-2">
    <div class="card reveal"><span class="eyebrow">Often helpful for</span><ul class="checklist" style="grid-template-columns:1fr">{"".join(f'<li>{icon("check")}<span>{g}</span></li>' for g in a["good_for"])}</ul></div>
    <div class="card reveal"><span class="eyebrow">What it feels like</span><p style="font-size:18px;color:var(--ink)">{a["feels"]}</p>
      <p class="small">Ben combines approaches within a session based on what your body needs, so you don't have to choose.</p>
      <a class="text-link" href="/first-visit/">What happens at a first visit {ARROW}</a></div>
  </div>
</section>
<section class="section"><div class="container">
  {section_head("Other approaches", "Ben often combines these in one session.")}
  <div class="grid grid-3">{others}</div>
</div></section>
{cta_final()}"""
    return body, schema


approach_cards = "".join(
    f'<a class="card card-link" href="/approaches/{a["slug"]}/">{icon(a["icon"], "card-icon")}<h3>{a["name"]}</h3><p>{a["short"]}</p><span class="text-link">Learn more {ARROW}</span></a>'
    for a in APPROACHES)
add("/approaches/", "Approaches: Structural Integration, Craniosacral, Visceral & Movement Work",
    "The methods Ben Walder uses and combines: Structural Integration (Rolfing), craniosacral therapy, visceral and neurovascular manipulation, and movement and breath education.",
    f"""
{page_hero("Approaches", "The methods behind the work.", "You don't need to choose a technique. Ben blends these in each session based on what your body needs. Here's what each one is, if you're curious.", crumbs=[("Approaches", None)], show_buttons=False)}
<section class="section"><div class="container"><div class="grid grid-2">{approach_cards}
<a class="card card-link" href="/herbal-nutrition/">{icon("leaf", "card-icon")}<h3>Herbal &amp; nutrition support</h3><p>Food, herbs, sleep and daily habits for recovery and resilience. In person or online.</p><span class="text-link">Learn more {ARROW}</span></a>
</div></div></section>
{cta_final()}""", crumb="Approaches")

for a in APPROACHES:
    b, s = approach_page(a)
    add(f"/approaches/{a['slug']}/", a["title"], a["desc"], b, crumb=a["name"].replace("&amp;", "&"), schema=s)


# ==========================================================================
# Ten-Series
# ==========================================================================
series_full = "".join(
    f'<li class="reveal"><span class="dot">{n}</span><span class="phase">{phase}</span><h4>Session {n}: {name}</h4><p>{text}</p></li>'
    for phase, n, name, text in TEN_SERIES)
TS_FAQS = [
    ("How often are Ten-Series sessions?", "<p>Usually once a week or every other week, so your body has time to integrate each session before the next. Ben will help you find a rhythm that fits your life.</p>"),
    ("Do I have to commit to all ten?", "<p>You can start with Session 1 and decide from there. Many people choose the prepaid package after their first session because it saves money.</p>"),
    ("What if I miss a week?", "<p>That's fine. The series is flexible. A longer gap just means a little more time reconnecting at the start of the next session.</p>"),
    ("What happens after the series?", "<p>Most people simply enjoy the results. Some come back for occasional tune-ups, especially athletes or anyone with a physical job.</p>"),
]
add("/ten-series/", "The Ten-Series: Structural Integration in 10 Sessions",
    "The Ten-Series is a ten-session, full-body Structural Integration sequence based on Dr. Ida Rolf's method, for lasting changes in posture, pain and movement. Price, sessions and FAQs.",
    f"""
{page_hero("The Ten-Series", "Ten sessions. Your whole body. Change that lasts.", "The most complete work Ben offers. Based on Dr. Ida Rolf's method, the Ten-Series reorganizes your body step by step, from the breath and outer layers, through the core, to a new, easier way of standing and moving.", crumbs=[("The Ten-Series", None)])}
<section class="section">
  <div class="container split" style="align-items:start">
    <div>
      <span class="eyebrow">Session by session</span>
      <h2>Each session builds on the last.</h2>
      <p class="muted">Three phases: free the outer &ldquo;sleeve,&rdquo; reorganize the core, then integrate it all.</p>
      <ol class="series mt-32">{series_full}</ol>
    </div>
    <div style="position:sticky;top:110px">
      <div class="price-card card--forest" style="margin-top:24px">
        <span class="flag">Prepaid package</span>
        <h3>The Ten-Series</h3><div class="duration">10 sessions · 60–75 min each</div>
        <div class="price">{ph("series")}</div>
        <ul><li>Saves {ph("$___")} vs. booking singly</li><li>Payment plan: {ph("3 × $___")}</li><li>HSA/FSA often accepted</li></ul>
        <a class="btn btn-primary" href="/pricing/#book">Start with Session 1</a>
      </div>
      <p class="small muted mt-32">Not sure yet? <a class="text-link" href="/contact/#call">Talk to Ben first {ARROW}</a></p>
    </div>
  </div>
</section>
<section class="section section--linen">
  <div class="container grid grid-2">
    <div class="card reveal"><span class="eyebrow">A great fit if</span>
      {checklist(["You've had pain or restriction for years", "You keep compensating for an old injury", "You want lasting change, not temporary relief", "You're an athlete or performer seeking better movement"]).replace('class="checklist"', 'class="checklist" style="grid-template-columns:1fr"')}</div>
    <div class="card reveal"><span class="eyebrow">Maybe not right now if</span>
      <ul class="checklist" style="grid-template-columns:1fr"><li>{icon("close")}<span>You only want occasional relaxation (try single sessions)</span></li><li>{icon("close")}<span>You're recovering from a recent injury or surgery (start gentler first)</span></li><li>{icon("close")}<span>You can't commit to roughly weekly sessions for a couple of months</span></li></ul></div>
  </div>
</section>
<section class="section">
  <div class="container split split--55" style="align-items:start">
    <div><span class="eyebrow">Questions</span><h2>About the Ten-Series.</h2></div>
    <div>{faq_block(TS_FAQS)}</div>
  </div>
</section>
{cta_final("Ready to start? Session 1 is all you need to decide.")}""",
    faqs=TS_FAQS, crumb="The Ten-Series",
    schema=[{"@context": "https://schema.org", "@type": "Service", "name": "The Ten-Series (Structural Integration)",
             "description": "A ten-session, full-body Structural Integration sequence based on Dr. Ida Rolf's method.",
             "provider": {"@id": "https://benwalder-redesign.onrender.com/#business"}, "areaServed": "North County San Diego"}])


# ==========================================================================
# Pricing & booking
# ==========================================================================
add("/pricing/", "Pricing & Booking",
    "Prices for first sessions, single sessions, the Ten-Series and herbal consultations with Ben Walder in North County San Diego. Book online, HSA/FSA often accepted.",
    f"""
{page_hero("Pricing &amp; booking", "Clear prices. Book in under a minute.", "Every option, what it includes, and a live calendar. HSA/FSA cards are often accepted, and receipts are provided for possible reimbursement.", crumbs=[("Pricing &amp; booking", None)], show_buttons=False)}
<section class="section section--linen"><div class="container">{price_cards()}</div></section>
<section class="section">
  <div class="container">
    {section_head("All options", "Every session type.")}
    <div class="table-wrap"><table>
      <thead><tr><th>Session</th><th>Length</th><th>Price</th><th>Best for</th></tr></thead>
      <tbody>
        <tr><td><strong>Discovery call</strong></td><td>15 min</td><td>Free</td><td>Not sure yet? Talk it through first.</td></tr>
        <tr><td><strong>First session</strong></td><td>90 min</td><td>{ph("first")}</td><td>Everyone new. History, assessment and hands-on work.</td></tr>
        <tr><td><strong>Single session</strong></td><td>60–75 min</td><td>{ph("single")}</td><td>Follow-ups and as-needed care.</td></tr>
        <tr><td><strong>The Ten-Series</strong></td><td>10 × 60–75 min</td><td>{ph("series")}</td><td>Lasting, whole-body change.</td></tr>
        <tr><td><strong>Herbal &amp; nutrition consult</strong></td><td>{ph("60 min")}</td><td>{ph("herbal")}</td><td>In person or online, anywhere.</td></tr>
        <tr><td><strong>Herbal follow-up</strong></td><td>{ph("30 min")}</td><td>{ph("$___")}</td><td>Adjusting your plan.</td></tr>
      </tbody>
    </table></div>
  </div>
</section>
<section class="section section--linen" id="book">
  <div class="container">
    {section_head("Book online", "Pick a time that works for you.", "You'll get a confirmation, a short intake form and a reminder before your visit.")}
    <div class="embed-ph">{icon("calendar")}<h3>Online booking calendar</h3>
      <p class="muted measure center">On the live site, Ben's Jane App (or Acuity) calendar embeds here, styled to match: live availability, intake forms, card on file and automatic reminders.</p>
      <div class="btn-row" style="justify-content:center"><a class="btn btn-secondary" href="/contact/#call">Prefer to call? {ph("phone")}</a></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container grid grid-3">
    <div class="card">{icon("shield", "card-icon")}<h3>Payment</h3><p>Cards, HSA/FSA (check your plan) and {ph("[other methods]")}. Payment is taken after your session.</p></div>
    <div class="card">{icon("calendar", "card-icon")}<h3>Cancellations</h3><p>Please give {ph("24 hours")} notice to reschedule or cancel, so someone else can use the time.</p></div>
    <div class="card">{icon("book", "card-icon")}<h3>Insurance</h3><p>Standard health insurance usually doesn't cover this work. Ben provides receipts and documentation for possible reimbursement.</p></div>
  </div>
</section>
{cta_final()}""", crumb="Pricing & booking")


# ==========================================================================
# First visit
# ==========================================================================
FV_FAQS = [FAQS_CORE[7], FAQS_CORE[3], FAQS_CORE[8]]
add("/first-visit/", "Your First Visit: What to Expect",
    "What happens at your first session with Ben Walder: what to wear, how long it takes, what the room is like, and what happens next.",
    f"""
{page_hero("Your first visit", "Here's exactly what happens at your first session.", "New to this kind of bodywork? Most people are. Here's what to expect, minute by minute, so there are no surprises.", crumbs=[("Your first visit", None)])}
<section class="section">
  <div class="container split" style="align-items:start">
    <div>
      <ol class="series">
        <li class="reveal"><span class="dot">1</span><span class="phase">Before</span><h4>Book and fill out a short form</h4><p>You'll get a quick intake form about your history and goals. Bring any relevant imaging or surgical notes.</p></li>
        <li class="reveal"><span class="dot">2</span><span class="phase">0–20 min</span><h4>Talk</h4><p>Ben asks about what's going on, what you've tried and what you want to get back to. Your story guides the work.</p></li>
        <li class="reveal"><span class="dot">3</span><span class="phase">20–30 min</span><h4>Look and move</h4><p>Ben watches how you stand, walk and breathe, to understand how your body is organized.</p></li>
        <li class="reveal"><span class="dot">4</span><span class="phase">30–80 min</span><h4>Hands-on work</h4><p>Slow, specific work on the table, sometimes seated or standing. You're always in control of the pressure.</p></li>
        <li class="reveal"><span class="dot">5</span><span class="phase">80–90 min</span><h4>Notice and plan</h4><p>You'll walk and notice what changed. Then you decide together on next steps, with no pressure.</p></li>
      </ol>
    </div>
    <div class="grid">
      {photo("The treatment room: table, natural light, a plant. Calm, clean, welcoming.", "", "wide")}
      <div class="embed-ph" style="padding:28px">{icon("chat")}<h3>60–90 second video</h3><p class="muted small mb-0">Ben explains what a session is like, in his own words. Filmed on the same day as the photo shoot.</p></div>
    </div>
  </div>
</section>
<section class="section section--linen">
  <div class="container grid grid-3">
    <div class="card">{icon("clock", "card-icon")}<h3>How long</h3><p>About 90 minutes for your first visit. Follow-ups are 60–75 minutes.</p></div>
    <div class="card">{icon("posture", "card-icon")}<h3>What to wear</h3><p>Shorts and a tank top or sports bra. Anything comfortable you can move in.</p></div>
    <div class="card">{icon("pin", "card-icon")}<h3>Getting here</h3><p>{ph("address")}. {ph("[Parking details]")}. <a class="text-link" href="/contact/">Directions</a></p></div>
  </div>
</section>
<section class="section"><div class="container split split--55" style="align-items:start">
  <div><span class="eyebrow">Questions</span><h2>Before you come in.</h2></div><div>{faq_block(FV_FAQS)}</div>
</div></section>
{cta_final()}""", faqs=FV_FAQS, crumb="Your first visit")


# ==========================================================================
# About
# ==========================================================================
add("/about/", "About Ben Walder",
    "Ben Walder came to bodywork through his own injury and chronic pain. 15 years of study in Structural Integration, manual therapy, Chinese medicine, herbalism and nutrition.",
    f"""
{page_hero("Meet Ben", "I came to this work the same way most of my clients do: in pain.", "15 years of study and practice in Structural Integration, manual therapy, Chinese medicine, herbalism and nutrition, all of it started by trying to solve my own injury.", crumbs=[("About", None)], show_buttons=False)}
<section class="section">
  <div class="container split" style="align-items:start">
    <div class="reveal" style="position:sticky;top:110px">{photo("Portrait of Ben, eye level, in the studio. Approachable, not corporate.")}</div>
    <div class="prose reveal">
      <p class="dropcap">An injury and years of chronic pain changed how I understand the body. I went looking for relief, and kept finding treatments that helped for a day or a week, then wore off. That frustration became curiosity, and the curiosity became my life's work.</p>
      <p>Over about 15 years I've studied Structural Integration, massage, Chinese medicine, craniosacral and visceral approaches, movement, herbalism, nutrition and nervous-system-oriented care. What ties it together is one idea: the body is one connected system, and it's always adapting.</p>
      <h2>How I work</h2>
      <ul>
        <li><strong>Understanding, not fixing.</strong> I see each session as a way to understand how your body has adapted over time, and to help it find a better option.</li>
        <li><strong>Your story leads.</strong> Your history and your feedback during the session guide what I do.</li>
        <li><strong>Teaching as I go.</strong> I want you to leave understanding your body better, not depending on me.</li>
      </ul>
      <h2>Training &amp; credentials</h2>
      <span class="ph-note">Ben to fill in: schools, certifications, dates</span>
      <ol class="series mt-32">
        <li><span class="dot">{icon("badge").replace('<svg', '<svg style="width:18px;height:18px"')}</span><span class="phase">{ph("Year")}</span><h4>Structural Integration certification</h4><p>{ph("[School / institute]")}</p></li>
        <li><span class="dot">{icon("badge").replace('<svg', '<svg style="width:18px;height:18px"')}</span><span class="phase">{ph("Year")}</span><h4>Craniosacral &amp; visceral training</h4><p>{ph("[Upledger / Barral Institute levels]")}</p></li>
        <li><span class="dot">{icon("badge").replace('<svg', '<svg style="width:18px;height:18px"')}</span><span class="phase">{ph("Year")}</span><h4>Massage therapy</h4><p>{ph("[School · CAMTC certificate #]")}</p></li>
        <li><span class="dot">{icon("leaf").replace('<svg', '<svg style="width:18px;height:18px"')}</span><span class="phase">{ph("Year")}</span><h4>Herbalism &amp; nutrition</h4><p>{ph("[Program / mentor]")}</p></li>
      </ol>
      <h2>Outside the studio</h2>
      <p>{ph("[A few lines about Ben's life: the garden, making remedies, time on the coast]")}</p>
      <p class="signature">— Ben</p>
      {buttons()}
    </div>
  </div>
</section>
<section class="section section--linen"><div class="container grid grid-3">
  {photo("Ben in conversation with a client, both seated, listening.", "", "square")}
  {photo("Dried herbs and tinctures on Ben's wooden worktable.", "sage", "square")}
  {photo("Morning on the North County coast.", "forest", "square")}
</div></section>
{cta_final()}""", crumb="About")


# ==========================================================================
# Results
# ==========================================================================
add("/results/", "Results & Client Stories",
    "Client stories from people who came to Ben Walder with chronic pain, old injuries, surgical scar tissue, posture problems and stress.",
    f"""
{page_hero("Results", "People come in after years of trying everything.", "Stories from clients with chronic pain, old injuries, scar tissue and stress, grouped so you can find people in a situation like yours.", crumbs=[("Results", None)], show_buttons=False,
  extra=f'<p class="mt-32 mb-0"><span class="stars">★★★★★</span> <strong>{ph("rating")}</strong> on Google from {ph("reviews")} reviews</p>')}
<section class="section">
  <div class="container">
    <div class="grid grid-2 reveal">
      {testimonial("20 years of back pain", "I'd lived with pain for over twenty years. Ben looked for the cause instead of chasing the symptom.")}
      {testimonial("A pelvis that healed wrong", "He found things through touch no one had noticed, and explained them so I understood my own body.")}
      {testimonial("Scar tissue from surgeries", "Warm, attentive and incredibly skilled. My scars move in ways they haven't in years.")}
      {testimonial("Knee injury", "My knee had never felt right since the injury. Now I forget about it most days.")}
      {testimonial("Stress held in the body", "I left feeling regulated in a way I hadn't in years. More personal than any massage I've had.")}
      {testimonial("Herbal support", "His knowledge of plants is remarkable. The remedies he made for me became part of my routine.")}
    </div>
  </div>
</section>
<section class="section section--linen">
  <div class="container">
    <div class="embed-ph">{icon("star")}<h3>Google reviews</h3><p class="muted measure center mb-0">Live Google reviews embed here once Ben's Business Profile is set up. Ask every client who finishes a Ten-Series for a review.</p></div>
  </div>
</section>
{cta_final("Your story could be next. Start with one session.")}""", crumb="Results")


# ==========================================================================
# FAQ
# ==========================================================================
add("/faq/", "Frequently Asked Questions",
    "Answers about Structural Integration, craniosacral and visceral work with Ben Walder: cost, insurance, what to wear, how many sessions, and whether it hurts.",
    f"""
{page_hero("FAQ", "Questions people ask before booking.", "Still unsure after reading? That's normal. A free 15-minute call is the easiest way to find out if this is for you.", crumbs=[("FAQ", None)], show_buttons=False)}
<section class="section"><div class="container split split--55" style="align-items:start">
  <div style="position:sticky;top:110px"><span class="eyebrow">Can't find it?</span><h2>Ask Ben directly.</h2><p class="muted">Skeptics welcome.</p>{buttons(("Book a free 15-min call", "/contact/#call"), None)}</div>
  <div>{faq_block(FAQS_CORE)}</div>
</div></section>
{cta_final()}""", faqs=FAQS_CORE, crumb="FAQ")


# ==========================================================================
# Herbal & nutrition
# ==========================================================================
HERB_FAQS = [
    ("Can I do a consultation online?", "<p>Yes. Consultations work just as well by video, so you can book from anywhere.</p>"),
    ("Do I have to buy herbs from you?", "<p>No. Ben can make custom formulations if you'd like, but he'll also help you source herbs from a grocery store, a trusted supplier or your own garden.</p>"),
    ("Is this safe with my medications?", "<p>Tell Ben about every medication and supplement you take. He'll factor that in, and recommend checking with your doctor or pharmacist where there could be an interaction.</p>"),
    ("Is this a diet?", "<p>No rigid diets. The focus is practical: meal structure, blood sugar, digestion, hydration and nourishing habits you can actually keep.</p>"),
]
add("/herbal-nutrition/", "Herbal & Nutrition Consultations, In Person or Online",
    "Personalized herbal and nutritional consultations with Ben Walder, in North County San Diego or online. Nervous system, sleep, recovery, digestion and inflammation support.",
    f"""
{page_hero("Herbal &amp; nutrition", "Herbal and nutrition support for recovery, sleep and resilience.", "Practical, personalized guidance on food, herbs, sleep and daily habits. In person in North County San Diego, or online from anywhere.", crumbs=[("Herbal &amp; nutrition", None)],
  extra='<p class="mt-32 mb-0"><span class="chip" style="margin:0">In person or online</span></p>')}
<section class="section">
  <div class="container split">
    <div class="reveal">{photo("Dried herbs, tinctures and Ben's hands on a wooden worktable.", "sage")}</div>
    <div class="reveal">
      <span class="eyebrow">What we work on</span>
      <h2>Support that fits your real life.</h2>
      <div class="grid grid-2 mt-32">
        <div><h4>Herbal support</h4><ul class="small muted"><li>Teas, kitchen herbs and tinctures</li><li>Nervous system and sleep</li><li>Inflammation, inside and out</li><li>Digestive bitters</li><li>Seasonal and immune support</li></ul></div>
        <div><h4>Nutrition</h4><ul class="small muted"><li>Meal structure and blood sugar</li><li>Digestion and hydration</li><li>Nutrient density</li><li>Cooking and sourcing food</li><li>Recovery and training</li></ul></div>
      </div>
    </div>
  </div>
</section>
<section class="section section--linen">
  <div class="container">
    {section_head("What you'll leave with", "Something you can actually use.", "", center=True)}
    <div class="grid grid-3">
      <div class="card">{icon("book", "card-icon")}<h3>A written plan</h3><p>Clear, simple recommendations you can follow without a nutrition degree.</p></div>
      <div class="card">{icon("leaf", "card-icon")}<h3>Herbs, your way</h3><p>A custom formulation if you want one, or guidance to source from your store or garden.</p></div>
      <div class="card">{icon("calendar", "card-icon")}<h3>Follow-up</h3><p>Optional check-ins to adjust as your body responds.</p></div>
    </div>
    <div class="price-cards mt-48" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">
      <div class="price-card"><h3>Initial consultation</h3><div class="duration">{ph("60 min")} · in person or online</div><div class="price">{ph("herbal")}</div><a class="btn btn-primary" href="/pricing/#book">Book a consultation</a></div>
      <div class="price-card"><h3>Follow-up</h3><div class="duration">{ph("30 min")} · in person or online</div><div class="price">{ph("$___")}</div><a class="btn btn-secondary" href="/pricing/#book">Book a follow-up</a></div>
    </div>
  </div>
</section>
<section class="section"><div class="container split split--55" style="align-items:start">
  <div><span class="eyebrow">Questions</span><h2>About consultations.</h2></div><div>{faq_block(HERB_FAQS)}
  <p class="disclaimer">Herbal and nutritional consultations are educational and supportive. They are not a substitute for medical diagnosis or treatment.</p></div>
</div></section>
{cta_final("Start with one conversation.", "Book an initial consultation in person or online.")}""", faqs=HERB_FAQS, crumb="Herbal & nutrition")


# ==========================================================================
# Contact
# ==========================================================================
add("/contact/", "Contact & Location",
    f"Contact Ben Walder Healing Arts in North County San Diego. Book a free 15-minute call, find directions and parking, or send a message.",
    f"""
{page_hero("Contact", "Let's talk about what's going on.", "Book a free 15-minute call, send a message, or find the studio.", crumbs=[("Contact", None)], show_buttons=False)}
<section class="section" id="call">
  <div class="container split" style="align-items:start">
    <div>
      <span class="eyebrow">Free 15-minute call</span>
      <h2>Not sure yet? Talk it through first.</h2>
      <p class="muted">Tell Ben what's going on and what you've tried. He'll tell you honestly whether he thinks he can help, and if not, who might.</p>
      <div class="embed-ph" style="text-align:left;padding:28px">{icon("calendar").replace('margin: 0 auto 14px', '')}<h3>Book a call</h3><p class="muted small">Discovery-call calendar embeds here on the live site.</p></div>
      <div class="grid grid-2 mt-32">
        <div class="card">{icon("phone", "card-icon")}<h3>Call or text</h3><p>{ph("phone")}</p></div>
        <div class="card">{icon("mail", "card-icon")}<h3>Email</h3><p><a class="text-link" href="mailto:hello@benwalder.com">hello@benwalder.com</a></p></div>
      </div>
    </div>
    <div>
      <span class="eyebrow">Send a message</span>
      <form class="form" data-concept>
        <div><label for="name">Name</label><input id="name" name="name" autocomplete="name" required></div>
        <div><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div><label for="phone">Phone (optional)</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
        <div><label for="msg">What's going on?</label><textarea id="msg" name="message" rows="5"></textarea></div>
        <button class="btn btn-primary" type="submit">Send message</button>
        <p class="form-note form-status">Ben usually replies within one business day.</p>
      </form>
    </div>
  </div>
</section>
<section class="section section--linen">
  <div class="container split">
    <div class="map-ph"><div>{icon("pin", "map-pin")}<strong>{ph("address")}</strong><p class="small muted mb-0">Google Map embeds here</p></div></div>
    <div>
      <span class="eyebrow">The studio</span>
      <h2>Finding Ben.</h2>
      <p>{ph("address")}</p>
      <p><strong>Hours:</strong> By appointment<br><strong>Parking:</strong> {ph("[Parking details]")}<br><strong>Serving:</strong> {ph("[Encinitas, Carlsbad, Oceanside, Vista, San Marcos…]")}</p>
      <a class="btn btn-secondary" href="#">Get directions</a>
    </div>
  </div>
</section>
{cta_final()}""", crumb="Contact")


# ==========================================================================
# Learn (articles)
# ==========================================================================
ARTICLES = [
    {
        "slug": "rolfing-vs-massage", "title": "Rolfing vs. Massage: What's the Difference?",
        "desc": "Rolfing (Structural Integration) and massage both use hands-on work, but they aim at different things. Here's how they differ and which one fits your situation.",
        "answer": "Massage mainly relaxes muscles and relieves tension in the areas that bother you. Rolfing, or Structural Integration, works more slowly across the whole body's fascia to change the posture and compensation patterns behind recurring pain. Massage is great for relief; Structural Integration aims for lasting structural change.",
        "body": """
<h2>What massage is best at</h2>
<p>A good massage relaxes tight muscles, improves circulation and calms the nervous system. It's excellent for stress relief and short-term relief of tension. Most massage focuses on the areas you point to.</p>
<h2>What Structural Integration is best at</h2>
<p>Structural Integration looks at how your whole body is organized: how your feet, pelvis, ribs and head stack and move together. It works with fascia, the connective tissue that holds that organization in place, using slower, more specific pressure, often while you move.</p>
<p>Instead of only relieving the spot that hurts, it aims to change the pattern that keeps loading that spot.</p>
<h2>Which one should you choose?</h2>
<ul><li><strong>Choose massage</strong> if you want relaxation, stress relief or occasional relief from everyday tension.</li>
<li><strong>Choose Structural Integration</strong> if the same pain keeps coming back, your posture won't hold, or you're compensating for an old injury.</li></ul>
<p>Many people enjoy both. Structural Integration can make the benefits of massage last longer.</p>""",
    },
    {
        "slug": "is-structural-integration-painful", "title": "Is Rolfing Painful? What Structural Integration Really Feels Like",
        "desc": "Rolfing has a reputation for being painful. Here's what modern Structural Integration actually feels like, and how practitioners like Ben keep it comfortable.",
        "answer": "Modern Structural Integration can feel intense in areas that have been restricted for a long time, but it shouldn't be painful in a way you can't tolerate. A good practitioner works with your feedback, adjusts pressure constantly, and you're always in control. Most people describe it as a strong, satisfying release.",
        "body": """
<h2>Where the reputation comes from</h2>
<p>Early Rolfing in the 1970s earned a reputation for being forceful. The field has changed a lot since then. Most practitioners today work more slowly and responsively, with the idea that the body changes more easily when it isn't defending itself.</p>
<h2>What it actually feels like</h2>
<p>Most of a session feels like slow, deep, specific pressure, often combined with small movements you make. Areas that have been stuck for years can feel intense, sometimes described as a &ldquo;good hurt&rdquo; or a stretch from the inside.</p>
<h2>How Ben keeps it comfortable</h2>
<ul><li>He checks in constantly and adjusts to your feedback.</li><li>He works with your breath, not against it.</li><li>He uses gentler craniosacral or visceral work when your body needs to settle first.</li><li>You can ask for less pressure at any moment.</li></ul>""",
    },
    {
        "slug": "how-many-sessions", "title": "How Many Structural Integration Sessions Do You Need?",
        "desc": "Some people feel a difference in one session, others benefit from the full Ten-Series. Here's how to think about how many Structural Integration sessions you need.",
        "answer": "It depends on your goals and how long the pattern has been there. Many people notice a change in one to three sessions. Longstanding pain, old injuries and posture issues usually respond best to a series, and the classic Ten-Series is designed for comprehensive, lasting change.",
        "body": """
<h2>One to three sessions</h2>
<p>A good starting point if you want to feel what the work does, or if you have a fairly recent, specific issue. Many people notice they breathe, stand or move differently after the first session.</p>
<h2>A short series (four to six sessions)</h2>
<p>Useful when there's a clear area of concern, like an old ankle injury affecting your knee and hip, and you want to work through the pattern around it.</p>
<h2>The Ten-Series</h2>
<p>The most complete option. It works through the whole body in a planned sequence, which is why it's often recommended for pain or posture problems that have been around for years. <a href="/ten-series/">See how the Ten-Series works</a>.</p>
<h2>No pressure either way</h2>
<p>Ben checks progress with you as you go and won't push you toward more sessions than you need.</p>""",
    },
    {
        "slug": "what-is-fascia", "title": "What Is Fascia, and Why Does It Matter for Pain?",
        "desc": "Fascia is the connective tissue that wraps and links every muscle and organ. Here's what it is, how it adapts, and why it matters for chronic pain and posture.",
        "answer": "Fascia is a continuous web of connective tissue that surrounds and links your muscles, bones, nerves and organs. It adapts to how you use your body, so injuries, habits and stress can leave it tight or stuck in ways that affect posture, movement and pain far from the original problem.",
        "body": """
<h2>A body-wide web</h2>
<p>Picture the white, filmy layer you see on a cut of meat. That's fascia. In your body it's a single continuous network, wrapping every muscle fiber, muscle, organ and nerve, and linking them together.</p>
<h2>Why it matters for pain</h2>
<p>Because it's all connected, a restriction in one place can pull on structures somewhere else. That's one reason pain can show up far from the original injury, and why treating only the sore spot often doesn't last.</p>
<h2>Fascia adapts</h2>
<p>Fascia responds to how you use your body. Hours at a desk, an old injury or long-term stress can leave it thicker, tighter or less able to glide. The good news: it keeps adapting throughout life, which is why hands-on work like Structural Integration can help it change.</p>""",
    },
]

article_cards = "".join(
    f'<a class="card card-link" href="/learn/{a["slug"]}/"><span class="eyebrow">Article</span><h3>{a["title"]}</h3><p>{a["desc"]}</p><span class="text-link">Read {ARROW}</span></a>'
    for a in ARTICLES)
add("/learn/", "Learn: Structural Integration, Fascia & Chronic Pain",
    "Plain-language articles on Structural Integration (Rolfing), fascia, chronic pain and what to expect from bodywork, from Ben Walder Healing Arts.",
    f"""
{page_hero("Learn", "Plain answers to the questions people actually search for.", "Short, honest articles about Structural Integration, fascia and chronic pain.", crumbs=[("Learn", None)], show_buttons=False)}
<section class="section"><div class="container"><div class="grid grid-2">{article_cards}</div>
<div class="card mt-48"><span class="eyebrow">Coming next</span><p class="mb-0">What Rolfing costs in San Diego · Craniosacral vs. visceral manipulation · Bodywork after a car accident · Structural Integration for surfers · Is Rolfing worth it?</p></div>
</div></section>
<section class="section section--forest"><div class="container split">
  <div><span class="eyebrow">Free guide</span><h2>5 reasons pain comes back after PT, and what to do instead.</h2><p class="lede">A short, practical guide from Ben. Delivered by email.</p></div>
  <form class="inline-form" data-concept><label class="sr-only" for="guide-email">Email</label><input class="" id="guide-email" type="email" placeholder="you@email.com" required style="min-height:52px;border-radius:10px;border:0;padding:0 14px;font:inherit"><button class="btn btn-primary" type="submit">Send me the guide</button><p class="form-status small" style="grid-column:1/-1;color:rgba(246,241,234,.75)">No spam. Unsubscribe anytime.</p></form>
</div></section>
{cta_final()}""", crumb="Learn")

for a in ARTICLES:
    schema = [{"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
               "author": {"@id": "https://benwalder-redesign.onrender.com/about/#ben"},
               "publisher": {"@id": "https://benwalder-redesign.onrender.com/#business"}}]
    add(f"/learn/{a['slug']}/", a["title"], a["desc"], f"""
{page_hero("Learn", a["title"], a["desc"], crumbs=[("Learn", "/learn/"), (a["title"], None)], show_buttons=False)}
<section class="section"><div class="container split split--55" style="align-items:start">
  <article class="prose">
    <div class="answer-box"><b>Short answer</b>{a["answer"]}</div>
    {a["body"]}
    <p class="disclaimer">Written by Ben Walder. Educational information, not medical advice.</p>
  </article>
  <aside style="position:sticky;top:110px"><div class="card">
    <span class="eyebrow">Have a question about your situation?</span>
    <h3>Talk to Ben for 15 minutes, free.</h3>
    <p>He'll tell you honestly whether this work is a good fit.</p>
    {buttons(("Book a free call", "/contact/#call"), ("See pricing", "/pricing/"))}
  </div></aside>
</div></section>
{cta_final()}""", crumb=a["title"], schema=schema)


# ==========================================================================
# 404
# ==========================================================================
add("/404/", "Page not found", "This page wandered off.", f"""
<section class="section"><div class="container center" style="max-width:640px">
  <span class="eyebrow">404</span><h1>This page wandered off.</h1>
  <p class="lede center">Let's get you back on track.</p>
  {buttons(("Go to the homepage", "/"), ("See what Ben helps with", "/conditions/"))}
</div></section>""")
