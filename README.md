# 🌎 Pathna Bot
Demo video: [link](https://youtu.be/)
<br>
Bot: [Warpcast profile](https://warpcast.com/pathnabot)
<br>
Farcaster client repo: [GitHub link](https://github.com/mainstreetlab/pathna-bot) (for farcaster client frontend)
<br>
<br>

# 🤖 About
A builder's bounties bot on the Farcaster client - Warpcast. Use `@pathnabot` in any bounties you post on Warpcast to record your bounties and get it distributed it via our app.
<br>
<br>
Examples commands:
- ` @pathnabot cancel`
- ` @pathnabot in progress`
- ` @pathnabot complete (optional: tag winners)`
- ` @pathnabot shoutout (optional: tag winner and write a positive review)`
    <br>
    <br>

# ❓ Problem
People struggle to get oppurtunities in web3. We are creating a distribution channel that matches users with oppurtunities. 
<br>
<br>
Builders in Africa want to get into web3 and gain access to oppurtunities so we built pathna to make them accessible. It's currently live, try it out! 🌎🚀
<br>
<br>

# 🛠️ Tech Stack
➔ farcaster-py: for detecting recent casts with the `"@pathnabot"` keyword, and posting confirmation responses
<br>
➔ OpenAI: for translating the actual text into the desired format on the Pathna App
<br>

When a user tags `@pathnabot`, the farcaster-py SDK will detect the cast. This cast has a `cast.text` property, and the `cast.parent_hash` property can be used to retrieve the parent cast's text. Both of these are either passed into OpenAI's API to generate an appropriate format and publishing confirmation message.
<br>
Users can post any bounty with the required key components which are: Task details, Deadline, Number of claims, Total prize pool/reward
<br>
Once a pathnabot cast is made, we use the farcaster-py SDK to help post an instant confirmation message.

# 🗺️ Road Map
1. Neynar APIs: use their webhooks and APIs for easier bot maintenance, and use Frames to improve the UX
2. OpenAI: finetune the AI model and provide better data/prompts for more accurate bounties formatting.
