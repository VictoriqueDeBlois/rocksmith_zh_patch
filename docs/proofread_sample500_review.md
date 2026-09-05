# Rocksmith 2014 译文 DS Flash 抽检审阅清单（487 组文本 / 样本 500 条 id）

> 本文档是给「另一个模型开新会话」阅读的审阅材料。请**不要修改仓库任何文件**，
> 只需阅读本清单并输出：①每条/每类要不要采纳 DS 改动；②归纳出的通用规则清单。

## 1. 背景（供审阅模型了解上下文）

- 项目：Rocksmith 2014 (Remastered) 中文化。把中文写入 `maingame.csv` 的 English 列，游戏英文语言下显示中文。
- 「现译」= 服务器 **qwen3.8** 生成的简体译文（`data/translations_remaining.json`，共 16067 条，已排除汉化组 4022 条）。
- 「DS」= **DeepSeek V4 Flash** 对本条提出的校对建议。
- 本清单样本：随机 500 条 id（seed=20260905），**已排除** 汉化组 4022 条 + 人工锁定 `data/proofread_manual.json`（116 条）。
- 已落地、**不要再当新问题报**的全局规则：
  1. 占位符 `{C} {B} {L} {X} {A} {0} {1} [1]` 是按键/图标，**必须保留**；DS 若删改占位符即为错误建议。
  2. `profile` 统一译「玩家档案」（已全局替换 102 条）。
  3. 音色/预设/风格名（Harmonic Minor Electronic 等）保持中文译名，不要改回英文。
  4. 术语：cab/box=箱体、amp=音箱、inline=联排、fret-hand mute=左手制音、slide=滑音。
  5. 代词：玩家用「你」；歌曲/物品用「它」，不用「她」。

## 2. 统计

- 唯一文本组数：487
- 「改动」（DS 建议 ≠ 现译）：**50**
- 「未改动」：437
- DS 结果缺失：0
- 其中已在 `data/proofread_sample500_changes.json` 记录的改动 id 数：50

## 3. 清单

| ID | 英文原文 | 现译（qwen3.8） | DS 建议 | 状态 |
|---|---|---|---|---|
| 5885 | Redeem Codes | 兑换代码 | 兑换代码 | 未改动 |
| 5902 | You have removed the storage device in use. You will now be returned to the main menu. | 已移除正在使用的存储设备。现在将返回主菜单。 | 已移除正在使用的存储设备。现在将返回主菜单。 | 未改动 |
| 5964 | Downloaded content will be available after you return to the Title Page. | 返回标题页面后，下载的内容将可用。 | 返回标题页面后，下载的内容将可用。 | 未改动 |
| 6034 | GOOD | 良好 | 良好 | 未改动 |
| 6041, 6591 | You cannot join this session. The host is using content that you have not yet downloaded. | 无法加入此会话。房主正在使用你尚未下载的内容。 | 无法加入此会话。房主正在使用你尚未下载的内容。 | 未改动 |
| 6085 | You have %d hour(s) left on your free trial. Activate your Uplay Passport to access online multiplayer. If your Uplay Passport code is missing or it has already been redeemed{C} you can buy a new one in the %s. | 你的免费试用还剩 %d 小时。激活你的 Uplay Passport 以访问在线多人模式。如果你的 Uplay Passport 代码缺失或已被兑换{C} 你可以在 %s 中购买新的代码。 | 你的免费试用还剩 %d 小时。激活你的 Uplay Passport 以访问在线多人模式。如果你的 Uplay Passport 代码缺失或已被兑换{C} 你可以在 %s 中购买新的代码。 | 未改动 |
| 6138 | Save failed. | 保存失败。 | 保存失败。 | 未改动 |
| 6177 | The code you entered is not valid. Please try again. | 您输入的代码无效。请重试。 | 你输入的代码无效。请重试。 | 改动 |
| 6209 | Do you really want to quit this session? | 确定要退出此会话吗？ | 确定要退出此会话吗？ | 未改动 |
| 6222 | To perform this operation{C} you must quit the game. You will lose any unsaved progress. Do you want to quit the game now? | 要执行此操作{C}你必须退出游戏。未保存的进度将会丢失。确定现在退出游戏吗？ | 要执行此操作{C}你必须退出游戏。未保存的进度将会丢失。确定现在退出游戏吗？ | 未改动 |
| 6258 | pointer | 指针 | 指针 | 未改动 |
| 6283 | obstruction | 障碍物 | 障碍物 | 未改动 |
| 6332 | No storage device has been selected. Your progress and settings will not be saved. | 未选择存储设备。您的进度和设置将不会被保存。 | 未选择存储设备。你的进度和设置将不会被保存。 | 改动 |
| 6372 | master account | 主账户 | 主账户 | 未改动 |
| 6379 | Xbox 360 console | Xbox 360 主机 | Xbox 360 主机 | 未改动 |
| 6393 | sub account | 子账号 | 子账号 | 未改动 |
| 6485 | Downloadable content %s corrupted. Content ignored. | 可下载内容 %s 已损坏。内容被忽略。 | 可下载内容 %s 已损坏。内容被忽略。 | 未改动 |
| 6528 | You need to be signed into Xbox LIVE to access Xbox LIVE game play features. | 你需要登录Xbox LIVE才能访问Xbox LIVE游戏功能。 | 你需要登录Xbox LIVE才能访问Xbox LIVE游戏功能。 | 未改动 |
| 6551 | This game saves data automatically at certain points. Do not switch off the power when this icon is displayed. | 此游戏会在特定点自动保存数据。显示此图标时请勿关闭电源。 | 此游戏会在特定点自动保存数据。显示此图标时请勿关闭电源。 | 未改动 |
| 6573 | Incorrect disc. | 光盘不正确。 | 光盘不正确。 | 未改动 |
| 6578 | A saved game already exists. Select "Continue" to overwrite or "Cancel" to continue without saving. | 已存在存档。选择“继续”以覆盖，或选择“取消”以不保存继续。 | 已存在存档。选择“继续”以覆盖，或选择“取消”以不保存继续。 | 未改动 |
| 6594 | HIGH / BAD | 高 / 差 | 高 / 差 | 未改动 |
| 6609 | PACKET LOST | 数据包丢失 | 数据包丢失 | 未改动 |
| 6636 | An error has occurred while accessing the System Cache. The game will restart. | 访问系统缓存时发生错误。游戏将重启。 | 访问系统缓存时发生错误。游戏将重启。 | 未改动 |
| 6647 | You cannot join this session because it is full. | 该场次已满，无法加入。 | 该场次已满，无法加入。 | 未改动 |
| 6668 | NAT CLASSIFICATION | NAT 分类 | NAT 分类 | 未改动 |
| 6694 | Your NAT type is OPEN (NAT Type 1). OPEN NAT is the optimal setting. You will join games and communicate with other players without experiencing any problems. | 你的 NAT 类型为开放型（NAT 类型 1）。开放型 NAT 是最佳设置。你将能够加入游戏并与其他玩家通信，且不会遇到任何问题。 | 你的 NAT 类型为开放型（NAT 类型 1）。开放型 NAT 是最佳设置。你将能够加入游戏并与其他玩家通信，且不会遇到任何问题。 | 未改动 |
| 6786 | You have been removed from the session by the group leader. | 你已被房主移出场次。 | 你已被房主移出场次。 | 未改动 |
| 6794 | You can play the [NAME OF THE CONTENT HERE IN CAPS] during the TRIAL PERIOD. If you want to continue playing when the Trial Period EXPIRES{C} get the FULL VERSION NOW. | 你可以在试用期内播放 [NAME OF THE CONTENT HERE IN CAPS]。如果你想在使用期 EXPIRES 后继续游玩{C}请立即获取 FULL VERSION NOW。 | 你可以在试用期内播放 [NAME OF THE CONTENT HERE IN CAPS]。如果你想在试用期到期后继续游玩{C}，请立即获取完整版。 | 改动 |
| 6799 | CONTINUE | 继续 | 继续 | 未改动 |
| 6802 | The group leader has changed. | 群组领导者已变更。 | 群组领导者已变更。 | 未改动 |
| 6869 | D-pad | 十字键 | 十字键 | 未改动 |
| 6873 | LT{C} RT | LT{C}RT | LT{C} RT | 改动 |
| 6896 | You have been returned to the main menu because another user with the same online ID has signed in. | 由于另一位使用相同在线ID的用户已登录，你已被返回主菜单。 | 由于另一位使用相同在线ID的用户已登录，你已被返回主菜单。 | 未改动 |
| 6954 | You have been returned to the single player mode due to a network error (%x). Make sure your network is correctly configured. | 由于网络错误（%x），你已被返回单人模式。请确保网络配置正确。 | 由于网络错误（%x），你已被返回单人模式。请确保网络配置正确。 | 未改动 |
| 7054 | Xbox 360 Wireless Headset | Xbox 360 无线耳机 | Xbox 360 无线耳机 | 未改动 |
| 7098 | You have been returned to the single player mode because an update to the PlayStation®Network is required. | 由于需要更新 PlayStation®Network，已返回单人模式。 | 由于需要更新 PlayStation®Network，你已被返回单人模式。 | 改动 |
| 7284 | PlayStation®Eye is not connected correctly. | PlayStation®Eye 未正确连接。 | PlayStation®Eye 未正确连接。 | 未改动 |
| 7329 | You are currently in this match. | 你当前正在参与此对局。 | 你当前正在参与此对局。 | 未改动 |
| 7351 | This game may send data automatically at certain points. Do not sign out of Xbox LIVE when this icon is displayed. | 此游戏可能会在特定时刻自动发送数据。当此图标显示时，请勿退出Xbox LIVE。 | 此游戏可能会在特定时刻自动发送数据。当此图标显示时，请勿退出Xbox LIVE。 | 未改动 |
| 7361 | Click the "News" floor button to see the latest information from Xbox LIVE{C} Uplay and Twitter | 点击“新闻”楼层按钮查看来自 Xbox LIVE{C} Uplay 和 Twitter 的最新信息 | 点击“新闻”楼层按钮查看来自 Xbox LIVE{C} Uplay 和 Twitter 的最新信息 | 未改动 |
| 7387 | Reach your left hand to HERE | 将左手伸到这里 | 将左手伸到这里 | 未改动 |
| 7393 | Slowly move your arm up {L}or down. | 缓慢地将手臂向上{L}或向下移动。 | 缓慢地将手臂向上{L}或向下移动。 | 未改动 |
| 7408 | The microphone volume can be adjusted in the Pause Menu. | 麦克风音量可在暂停菜单中调整。 | 麦克风音量可在暂停菜单中调整。 | 未改动 |
| 7508 | You must be connected to Xbox LIVE in order to access Xbox LIVE functionality. | 你必须连接Xbox LIVE才能访问Xbox LIVE功能。 | 你必须连接Xbox LIVE才能访问Xbox LIVE功能。 | 未改动 |
| 7516 | Open your match to the public?{L}{L}Allows everyone to join and the match will start automatically. | 将您的比赛对公众开放？{L}{L}允许所有人加入，比赛将自动开始。 | 将你的比赛对公众开放？{L}{L}允许所有人加入，比赛将自动开始。 | 改动 |
| 7524 | This feature requires you to be connected to Xbox LIVE. | 此功能要求你已连接 Xbox LIVE。 | 此功能要求你已连接 Xbox LIVE。 | 未改动 |
| 7530 | Your connection to Xbox LIVE has been lost. | 你与 Xbox LIVE 的连接已断开。 | 你与 Xbox LIVE 的连接已断开。 | 未改动 |
| 7535 | Failed to create a match.  The connection is not responding. | 创建匹配失败。连接无响应。 | 创建匹配失败。连接无响应。 | 未改动 |
| 7551 | Signed into Xbox LIVE | 已登录 Xbox LIVE | 已登录 Xbox LIVE | 未改动 |
| 7563 | Press {Img.StartButton.IK_JOY8} to start matchmaking. | 按 {Img.StartButton.IK_JOY8} 开始匹配。 | 按 {Img.StartButton.IK_JOY8} 开始匹配。 | 未改动 |
| 7570 | TrueSkill™ rank | TrueSkill™ 等级 | TrueSkill™ 等级 | 未改动 |
| 7582 | quick match | 快速匹配 | 快速匹配 | 未改动 |
| 7599 | Xbox Guide | Xbox 指南 | Xbox 指南 | 未改动 |
| 7626 | game chat | 游戏聊天 | 游戏聊天 | 未改动 |
| 7632 | friends list | 好友列表 | 好友列表 | 未改动 |
| 7680 | invite | 邀请 | 邀请 | 未改动 |
| 7755 | Save Game | 保存游戏 | 保存游戏 | 未改动 |
| 7756 | Unlock Full Game | 解锁完整游戏 | 解锁完整游戏 | 未改动 |
| 7767 | Download Content | 下载内容 | 下载内容 | 未改动 |
| 8267 | Be sure both fingers come down at the same time so you get that minor-7 sound coming in all at once{C} nice and clean. | 确保两根手指同时落下，以便一次性发出干净的 minor-7 声音{C} 清晰悦耳。 | 确保两根手指同时落下，以便小七和弦的声音一起发出{C}，干净利落。 | 改动 |
| 8404 | One thing about bends is that they can only really go up from where you start. But sometimes you might want to get that bend sound with a falling note.  For that{C} you can use pre-bends. | 关于推弦的一点是，它们通常只能从起始位置向上推。但有时你可能想要那种音符下落的推弦效果。为此{C}你可以使用预推弦。 | 关于推弦的一点是，它们只能从起始位置向上推。但有时你可能想要那种音符下落的推弦效果。为此{C}你可以使用预推弦。 | 改动 |
| 8409 | Once you've got the string bent the right amount{C} there's really nothing to it. | 一旦你把琴弦推到正确的程度{C}其实没什么难的。 | 一旦你把琴弦推到正确的程度{C}其实没什么难的。 | 未改动 |
| 8437 | Alright{C} now the tricky part. You've got to bend the note with your third finger{C} without picking up your first finger or accidently muting the other string. | 好了{C}现在是难点部分。你必须用第三根手指推弦{C}同时保持第一根手指不动，也不要意外闷住另一根弦。 | 好了{C}现在是难点部分。你必须用第三根手指推弦{C}同时保持第一根手指不动，也不要意外闷住另一根弦。 | 未改动 |
| 8500 | It's just what it sounds like. You deaden the string with your fretting hand and then pick it. | 正如字面意思所示。你用按弦手制音，然后拨弦。 | 正如字面意思所示。你用按弦手制音，然后拨弦。 | 未改动 |
| 9204 | You don't want to pull it hard enough to change the pitch{C} you're just going for a little pluck as you release. | 你不需要用力拉弦来改变音高{C}，你只是在松手时轻轻拨动一下。 | 你不需要用力拉弦来改变音高{C}，你只是在松手时轻轻拨动一下。 | 未改动 |
| 9272 | The first dot is usually on the 3rd fret. Go ahead and find that on your guitar. | 第一个圆点通常在第 3 品。请在你的吉他上找到它。 | 第一个圆点通常在第 3 品。请在你的吉他上找到它。 | 未改动 |
| 9391 | Good{C} now let's try a few of those palm muted power chords in a row. | 不错{C}现在让我们连续演奏几个闷音强力和弦。 | 不错{C}现在让我们连续演奏几个闷音强力和弦。 | 未改动 |
| 9572 | Start with your first finger on the 3rd fret of the A string. | 食指放在 A 弦第 3 品。 | 先把食指放在 A 弦第 3 品。 | 改动 |
| 9582 | Using that same basic power chord shape{C} you can add one more note to get a slightly beefier sound. | 使用同样的基础强力和弦指型{C}你可以再添加一个音符，获得更厚重的声音。 | 使用同样的基础强力和弦指型{C}你可以再添加一个音符，获得更厚重的声音。 | 未改动 |
| 9602 | Also{C} just like the other power chords{C} you can decide to keep in or leave out the upper octave note. | 另外{C}就像其他强力和弦一样{C}你可以决定保留或省略高八度音符。 | 另外{C}就像其他强力和弦一样{C}你可以决定保留或省略高八度音符。 | 未改动 |
| 9632 | Let's play that one note at a time. | 让我们逐个音符演奏。 | 让我们逐个音符演奏。 | 未改动 |
| 9669 | Then you can also fill in with up-strums between the beats... we'll call those upbeats. | 然后你可以在节拍之间加入上扫弦……我们称之为弱拍。 | 然后你可以在节拍之间加入上扫弦……我们称之为弱拍。 | 未改动 |
| 9732 | Now let's just try going back and forth between those two notes. Play along with this. | 现在让我们试着在这两个音符之间来回切换。跟着这个一起演奏。 | 现在让我们试着在这两个音符之间来回切换。跟着这个一起演奏。 | 未改动 |
| 9865 | You can barre just two strings... | 你只需要横按两根琴弦... | 你只需要横按两根琴弦... | 未改动 |
| 9885 | Let's focus on your first finger to start with. | 让我们先从你的食指开始练习。 | 让我们先从你的食指开始练习。 | 未改动 |
| 10158 | That's right ... what used to be your picking hand comes up to the fretboard and taps the fret. | 没错……原本负责拨弦的手现在要移到指板上，敲击琴品。 | 没错……原本负责拨弦的手现在要移到指板上，敲击琴品。 | 未改动 |
| 10385 | Others are attached with a strap. | 其他部分用背带固定。 | 其他部分用背带固定。 | 未改动 |
| 10504 | Guitar picks come in a variety of shapes and thicknesses. | 拨片有多种形状和厚度。 | 拨片有多种形状和厚度。 | 未改动 |
| 10657 | Nothing wrong with that{C} but let's try it with all the notes played short - or "staccato"{C} in music talk. | 这没什么问题{C}但让我们试试将所有音符演奏得短促一些——或者用音乐术语来说叫“断奏”{C}。 | 这没什么问题{C}但让我们试试将所有音符演奏得短促一些——或者用音乐术语来说叫“断奏”{C}。 | 未改动 |
| 10918 | It starts with just a regular bend. You bend it up a half-step{C} and then you let it come back down. | 它始于一个普通的推弦。你向上推半音{C} 然后让它回落。 | 它始于一个普通的推弦。你向上推半音{C} 然后让它回落。 | 未改动 |
| 11238 | If you're playing with your fingers{C} you'll just pick one string with each finger. | 如果你是用手指弹奏{C}你只需要用每根手指拨响一根琴弦。 | 如果你是用手指弹奏{C}你只需要用每根手指拨响一根琴弦。 | 未改动 |
| 11328 | The important thing is that you keep the string from vibrating. | 关键在于让琴弦停止振动。 | 关键在于让琴弦停止振动。 | 未改动 |
| 11772 | Alright{C} let's dive into this slide. | 好的{C} 让我们深入这个滑音。 | 好的{C} 让我们深入这个滑音。 | 未改动 |
| 11837 | Sometimes you play notes that fall on the beat{C} and sometimes you play notes that are off the beats. When the notes are off the beats{C} we call it "syncopation." | 有时你演奏落在节拍上的音符{C}有时你演奏不在节拍上的音符。当音符不在节拍上时{C}我们称之为“切分音”。 | 有时你演奏落在节拍上的音符{C}有时你演奏不在节拍上的音符。当音符不在节拍上时{C}我们称之为“切分音”。 | 未改动 |
| 12029 | That'll leave that open string ringing after you let it go{C} but you can also use this technique to pull off to another fingered note. | 这样会在你松开手指后让空弦继续共鸣{C} 但你也可以利用这个技巧滑向另一个按指的音符。 | 这样会在你松开手指后让空弦继续共鸣{C} 但你也可以利用这个技巧勾弦弹奏另一个按指的音符。 | 改动 |
| 12489 | If you want to do it yourself{C} though{C} here's how. | 如果你想自己动手{C}不过{C}方法如下。 | 如果你想自己动手{C}，不过{C}，方法如下。 | 改动 |
| 12493 | Keep in mind that basses are designed to be strung in different ways. We'll demonstrate with this bass{C} but yours may work differently{C} and you'll have to account for that. If you're unsure what to do{C} your local guitar shop guy will probably be glad to help you out. | 请记住，贝斯的设计允许不同的弦序方式。我们将以这把贝斯为例进行演示{C} 但你的乐器可能有所不同{C} 你需要对此加以考虑。如果你不确定该怎么做{C} 当地的吉他店店员通常会很乐意帮助你。 | 请记住，贝斯的设计允许不同的弦序方式。我们将以这把贝斯为例进行演示{C} 但你的乐器可能有所不同{C} 你需要对此加以考虑。如果你不确定该怎么做{C} 当地的吉他店店员通常会很乐意帮助你。 | 未改动 |
| 12749 | The most noticeable differences are that they have more or bigger speakers{C} and the speaker cabinets are more heavy-duty. | 最明显的区别是它们拥有更多或更大的扬声器{C} 且音箱箱体更加坚固耐用。 | 最明显的区别是它们拥有更多或更大的扬声器{C} 且音箱箱体更加坚固耐用。 | 未改动 |
| 13038 | Let's take a minute and go over the basic down stroke. That just means that you pick down through the string. | 花一分钟复习一下基本的下拨。意思就是向下扫过琴弦。 | 花一分钟复习一下基本的下拨。意思就是向下拨动琴弦。 | 改动 |
| 13077 | Here's the riff again. Listen to it{C} then play it. | 乐句又来了。先听一遍{C} 然后弹奏它。 | 乐句又来了。先听一遍{C} 然后弹奏它。 | 未改动 |
| 13108 | Now let your forearm rest lightly against the edge of the body{C} and you're ready to play. | 现在让前臂轻轻靠在琴身边缘{C}你就准备好演奏了。 | 现在让前臂轻轻靠在琴身边缘{C}你就准备好演奏了。 | 未改动 |
| 13183 | Ok{C} here goes. | 好的{C}开始了。 | 好的{C}开始了。 | 未改动 |
| 13235 | Not all guitars have the strap buttons in these exact locations{C} so you might have to adjust accordingly. | 并非所有吉他的背带扣都位于这些确切位置{C}因此你可能需要相应调整。 | 并非所有吉他的背带扣都位于这些确切位置{C}因此你可能需要相应调整。 | 未改动 |
| 13370 | OK{C} now let's put it all together in a song. | 好的{C} 现在让我们把这些组合成一首歌。 | 好的{C} 现在让我们把这些组合成一首歌。 | 未改动 |
| 13396 | Now your turn. | 现在轮到你了。 | 现在轮到你了。 | 未改动 |
| 13576 | Here's one more arpeggio pattern for you to try. | 这是另一个供你尝试的分解和弦模式。 | 这是另一个供你尝试的分解和弦模式。 | 未改动 |
| 13605 | ... and then your third and fourth fingers play the 14th fret on the A and D strings. | ... 然后你的第三和第四指按在 A 弦和 D 弦的第 14 品。 | ... 然后你的第三和第四指按在 A 弦和 D 弦的第 14 品。 | 未改动 |
| 17275 | EXTERNAL SPEAKERS{C} HOME THEATER{C} OR HEADPHONES | 外置扬声器{C}家庭影院{C}或耳机 | 外置扬声器{C}家庭影院{C}或耳机 | 未改动 |
| 17294 | Don't hold back. Keep strumming the strings repeatedly until you fill up the meter. To make more noise{C} strum harder. | 不要保留实力。反复扫弦直到填满计量表。要制造更多噪音{C}就用力扫弦。 | 不要保留实力。反复扫弦直到填满计量表。要制造更多噪音{C}就用力扫弦。 | 未改动 |
| 17506 | Make sure you're playing the note on the highlighted string and fret. | 确保你在高亮显示的琴弦和品位上弹奏音符。 | 确保你在高亮显示的琴弦和品上弹奏音符。 | 改动 |
| 17554 | If you'd like to change up the songs in your setlist{C} you can add{C} remove or replace songs using the menu options. Make sure to check the setlist details for the minimum and maximum songs allowed for each Event. | 如果你想更改歌单中的歌曲{C}你可以添加{C}移除或替换歌曲，请使用菜单选项。请务必查看歌单详情，了解每个活动允许的最少和最多歌曲数量。 | 如果你想更改歌单中的歌曲{C}你可以添加{C}移除或替换歌曲，请使用菜单选项。请务必查看歌单详情，了解每个活动允许的最少和最多歌曲数量。 | 未改动 |
| 17580 | Access the Guitar Menu Control Guide in the Options Menu. | 在选项菜单中访问吉他菜单控制指南。 | 在选项菜单中访问吉他菜单控制指南。 | 未改动 |
| 17600 | REHEARSED | 已排练 | 已排练 | 未改动 |
| 17606 | New Authentic Tone Unlocked: | 解锁新真实音色： | 解锁新真实音色： | 未改动 |
| 17637 | Unlocked Riff Repeater | 已解锁乐句重复器 | 已解锁乐句重复器 | 未改动 |
| 17660 | You just became a Chord Specialist. | 你刚刚成为了和弦专家。 | 你刚刚成为了和弦专家。 | 未改动 |
| 17676 | Rocksmith Points Reward | Rocksmith 点数奖励 | Rocksmith 点数奖励 | 未改动 |
| 17701 | Rehearse | 排练 | 排练 | 未改动 |
| 17707 | Remove Song | 移除歌曲 | 移除歌曲 | 未改动 |
| 17713 | Choose Songs | 选择歌曲 | 选择歌曲 | 未改动 |
| 17819 | Unplugged Mode unlocked for this song. Play without notes and shatter the score barrier! | 此歌曲已解锁不插电模式。无需跟随音符演奏，打破得分极限！ | 此歌曲已解锁不插电模式。无需跟随音符演奏，打破得分极限！ | 未改动 |
| 17885, 34252 | Barre Chords | 横按和弦 | 横按和弦 | 未改动 |
| 17899 | SCORE | 得分 | 得分 | 未改动 |
| 17938 | Level Up! | 升级！ | 升级！ | 未改动 |
| 17943 | TRACKER | 追踪器 | 追踪器 | 未改动 |
| 18017 | Perfect{L}Phrase | 完美{L}乐句 | 完美{L}乐句 | 未改动 |
| 18030, 18045, 18098, 18131, 18171, 18180, 18190, 18203, 20230, 20246 | TBD | 待定 | 待定 | 未改动 |
| 18078 | Hot! | 火热！ | 火热！ | 未改动 |
| 18175 | Squeal{L}Missed! | 刺耳声{L}失误！ | 刺耳声{L}失误！ | 未改动 |
| 18214 | New{L}High{L}Score! | 新{L}高{L}分！ | 新{L}高{L}分！ | 未改动 |
| 18339 | Pre Bridge [1] | 前桥段 [1] | 前桥段 [1] | 未改动 |
| 18396 | This is the E-major chord shape. | 这是E大调和弦的指型。 | 这是E大调和弦的指型。 | 未改动 |
| 18436 | This chord does not include the red and yellow strings. | 此和弦不包含红色和黄色琴弦。 | 此和弦不包含红色和黄色琴弦。 | 未改动 |
| 18442 | Strum those four strings when the D-major chord on the noteway hits the strings on the screen. | 当音符道上的 D 大调和弦到达屏幕上的琴弦时，扫这四根弦。 | 当音符道上的 D 大调和弦到达屏幕上的琴弦时，扫这四根弦。 | 未改动 |
| 18536 | These are hammer-ons. | 这些是击弦。 | 这些是击弦。 | 未改动 |
| 18584 | You make the shape by barre-ing your 1st finger along the red{C} yellow{C} and blue strings. | 用你的食指横按红色{C} 黄色{C} 和蓝色琴弦来形成这个形状。 | 用你的食指横按红色{C} 黄色{C} 和蓝色琴弦来形成这个形状。 | 未改动 |
| 18632 | Perfect. | 完美。 | 完美。 | 未改动 |
| 18703 | Experiment with downpicking and alternate picking to see what technique works best for you in the game. | 尝试下拨和交替拨弦，看看哪种技巧在游戏中最适合你。 | 尝试下拨和交替拨弦，看看哪种技巧在游戏中最适合你。 | 未改动 |
| 18707 | Looking at the top side of the neck{C} you'll see small dots which label specific frets. | 观察琴颈的顶部{C}你会看到标记特定品位的小圆点。 | 观察琴颈的顶部{C}你会看到标记特定品位的小圆点。 | 未改动 |
| 18710 | For every dot along the neck{C} there are matching inlays along the fretboard. | 琴颈上的每一个圆点{C}在指板上都有对应的镶嵌标记。 | 琴颈上的每一个圆点{C}在指板上都有对应的镶嵌标记。 | 未改动 |
| 18714 | As you play a song{C} notes may shift dramatically to another area of the fretboard{C} especially during solos. | 当你演奏歌曲时{C} 音符可能会大幅移动到指板的另一个区域{C} 尤其是在独奏部分。 | 当你演奏歌曲时{C} 音符可能会大幅移动到指板的另一个区域{C} 尤其是在独奏部分。 | 未改动 |
| 18783 | Take the new string out of the package. | 把新琴弦从包装中取出。 | 把新琴弦从包装中取出。 | 未改动 |
| 18875 | Learn the basics of playing chords. | 学习和弦演奏的基础知识。 | 学习和弦演奏的基础知识。 | 未改动 |
| 18906 | Changing your thumb position can make barre chords easier to play. | 改变拇指位置可以让横按和弦更容易弹奏。 | 改变拇指位置可以让横按和弦更容易弹奏。 | 未改动 |
| 18931 | These are chord hits. | 这些是和弦击打。 | 这些是和弦击打。 | 未改动 |
| 18943 | Play the green highlighted string now. | 现在演奏绿色高亮的琴弦。 | 现在演奏绿色高亮的琴弦。 | 未改动 |
| 18949 | Play the note on the green highlighted string now. | 现在演奏绿色高亮琴弦上的音符。 | 现在演奏绿色高亮琴弦上的音符。 | 未改动 |
| 19038 | SILVER | 银色 | 银色 | 未改动 |
| 19059 | CHORDS | 和弦 | 和弦 | 未改动 |
| 19066 | Body | 琴体 | 琴体 | 未改动 |
| 19073 | Frets | 品 | 品 | 未改动 |
| 19102 | Excellent! Next{C} play the orange one. | 很好！接下来{C} 演奏橙色音符。 | 很好！接下来{C} 演奏橙色音符。 | 未改动 |
| 19166 | Learn{C} practice{C} and master open chords. | 学习{C}练习{C}并掌握开放和弦。 | 学习{C}练习{C}并掌握开放和弦。 | 未改动 |
| 19169 | Play Video | 播放视频 | 播放视频 | 未改动 |
| 19179 | Results | 结果 | 结果 | 未改动 |
| 19332 | Play the right notes to shoot the Ducks before they fly away! | 在鸭子飞走前演奏正确的音符射击它们！ | 在鸭子飞走前演奏正确的音符射击它们！ | 未改动 |
| 19771 | No time bonus! | 没有时间奖励！ | 没有时间奖励！ | 未改动 |
| 19788 | Your new best score $score | 你的新最高分 $score | 你的新最高分 $score | 未改动 |
| 19945 | 3{C}2{C}1 {C} Dash! | 3{C}2{C}1 {C} 冲刺！ | 3{C}2{C}1 {C} 冲刺！ | 未改动 |
| 20031 | Play the right note! | 弹奏正确的音符！ | 弹奏正确的音符！ | 未改动 |
| 20032 | Tremolo to run! | 颤音跑起来！ | 颤音跑起来！ | 未改动 |
| 20040 | PLAYED | 已弹奏 | 已弹奏 | 未改动 |
| 20047 | Pick the string fast to run! | 快速拨弦以奔跑！ | 快速拨弦以奔跑！ | 未改动 |
| 20065 | PRESS THE START BUTTON | 按下开始按钮 | 按下开始按钮 | 未改动 |
| 20066 | Select a Scale | 选择音阶 | 选择音阶 | 未改动 |
| 20091 | Am | Am | Am | 未改动 |
| 20283 | [player name] unlocked the [amp name] | [player name] 解锁了 [amp name] | [player name] 解锁了 [amp name] | 未改动 |
| 20412 | Sound & Display Settings | 声音与显示设置 | 声音与显示设置 | 未改动 |
| 20450 | Set the on-screen guitar strings to the standard layout. | 将屏幕上的吉他琴弦设置为标准布局。 | 将屏幕上的吉他琴弦设置为标准布局。 | 未改动 |
| 20454 | Choose this option to use the currently active custom tone as the starting tone in every arrangement. | 选择此选项以将当前激活的自定义音色作为每个编曲的起始音色。 | 选择此选项以将当前激活的自定义音色作为每个编曲的起始音色。 | 未改动 |
| 20949 | Note: This parameter is only enabled if the Shape is set to Square. | 注意：仅当形状设置为方形时，此参数才启用。 | 注意：仅当形状设置为方形时，此参数才启用。 | 未改动 |
| 21019 | Filter | 滤波器 | 滤波器 | 未改动 |
| 21056 | Balancing Volume | 平衡音量 | 平衡音量 | 未改动 |
| 21067 | Enter Tone Name | 输入音色名称 | 输入音色名称 | 未改动 |
| 21074 | Choose from a list of authentic song tone presets. | 从一系列真实的歌曲音色预设中进行选择。 | 从一系列真实的歌曲音色预设中进行选择。 | 未改动 |
| 21155 | press the X Button | 按下 X 键 | 按下 X 键 | 未改动 |
| 21163 | press the square button | 按下方块键 | 按下方块键 | 未改动 |
| 21167 | press the L1 button | 按下 L1 键 | 按下 L1 键 | 未改动 |
| 21222 | Gold Technique Medals: [1] of [2] | 金牌技巧奖章：[1] / [2] | 金牌技巧奖章：[1] / [2] | 未改动 |
| 21226 | Gold Master Badges:  [1] of [2] | 金牌大师徽章：  [1] / [2] | 金牌大师徽章：  [1] / [2] | 未改动 |
| 21238 | Continue | 继续 | 继续 | 未改动 |
| 21240 | Storage Device Removed | 存储设备已移除 | 存储设备已移除 | 未改动 |
| 21280 | Sign in to PlayStation®Network to access online features of this title. | 登录 PlayStation®Network 以访问本游戏的在线功能。 | 登录 PlayStation®Network 以访问本游戏的在线功能。 | 未改动 |
| 21564 | Gibson Melody Maker | Gibson Melody Maker | Gibson Melody Maker | 未改动 |
| 21651 | You've been invited to play at a new bar. | 你被邀请到一家新酒吧演出。 | 你被邀请到一家新酒吧演出。 | 未改动 |
| 21714 | [Name] Roadhouse | [Name] 路边酒馆 | [Name] 路边酒馆 | 未改动 |
| 21733 | Club Liberty | 自由俱乐部 | Club Liberty | 改动 |
| 21769 | You've been invited to play at The Regency.{L}{L}To access your suggested setlist for this venue{C} go to the Event Manager. | 你被邀请去The Regency演出。{L}{L}要访问这个Venue的建议歌单{C}请前往Event Manager。 | 你被邀请去The Regency演出。{L}{L}要访问这个场馆的建议歌单{C}请前往活动管理器。 | 改动 |
| 21796 | Beat 15{C}000{C}000 points in the Guitarcade game: Super Slider | 在吉他街机游戏《Super Slider》中{C}获得15{C}000000分 | 在吉他街机游戏《Super Slider》中，获得超过15{C}000{C}000分 | 改动 |
| 21803 | Guitardead | Guitardead | Guitardead | 未改动 |
| 21840 | Qualify for a Double Encore | 达成双重安可条件 | 达成双重安可条件 | 未改动 |
| 21849 | D-licious | D-licious | D-licious | 未改动 |
| 21853 | Just Awesome | 非常棒 | 非常棒 | 未改动 |
| 21895 | The Rocksmith AutoWah | Rocksmith 自动哇音 | Rocksmith 自动哇音 | 未改动 |
| 21899 | The Rocksmith Distortion Pedal | Rocksmith 失真效果器 | Rocksmith 失真效果器 | 未改动 |
| 21955 | The Rocksmith Hitmacchen | Rocksmith Hitmacchen | Rocksmith Hitmacchen | 未改动 |
| 21966 | The Rocksmith Megan1X12 | Rocksmith Megan1X12 | Rocksmith Megan1X12 | 未改动 |
| 21983 | Achieved by muting and picking at the same time{C} palm muting is a technique used to create a percussive sound against the strings. | 通过同时制音和拨弦获得{C} 手掌制音是一种用于在琴弦上制造打击乐声音的技巧。 | 通过同时制音和拨弦获得{C} 手掌制音是一种用于在琴弦上制造打击乐声音的技巧。 | 未改动 |
| 21985 | Harmonics are pure{C} bell-like tones that can be produced by lightly touching the string over certain frets. | 泛音是纯净的{C} 钟鸣般的音色，可以通过轻触特定品上的琴弦产生。 | 泛音是纯净的{C}钟鸣般的音色，可以通过轻触特定品上的琴弦产生。 | 改动 |
| 21992 | New Technique Unlocked: Double Stops | 解锁新技术：双音 | 解锁新技术：双音 | 未改动 |
| 22028 | [1]  - Rocksmith Original Song | [1]  - Rocksmith 原创歌曲 | [1]  - Rocksmith 原创歌曲 | 未改动 |
| 22048 | n/a | 不适用 | 不适用 | 未改动 |
| 22070 | Sign-in as Guest | 以访客身份登录 | 以访客身份登录 | 未改动 |
| 22100 | Friends Scores | 好友分数 | 好友分数 | 未改动 |
| 22120 | Shift your hand as a single unit | 将手作为一个整体移动 | 将手作为一个整体移动 | 未改动 |
| 22133 | Fret the string with a feather-light touch and avoid pressing down too hard | 用轻柔的力度按弦，避免用力过猛 | 用轻柔的力度按弦，避免用力过猛 | 未改动 |
| 22139 | Make sure your other fingers aren’t accidentally touching other strings | 确保你的其他手指没有意外触碰到其他琴弦 | 确保你的其他手指没有意外触碰到其他琴弦 | 未改动 |
| 22255 | A pop is performed by using a plucking type motion. | Pop 音通过拨弦动作演奏。 | Pop 音通过拨弦动作演奏。 | 未改动 |
| 22269 | Then{C} with your palm still down{C} pick the string. | 然后{C}保持手掌向下{C}拨动琴弦。 | 然后{C}保持手掌向下{C}拨动琴弦。 | 未改动 |
| 22301 | Welcome to Soundcheck.  Here we’ll test out your bass’s volume{C} check the tuning{C} and play a few practice notes. | 欢迎来到声音检查。在这里我们将测试你的贝斯音量{C}检查调弦{C}并演奏几个练习音符。 | 欢迎来到声音检查。在这里我们将测试你的贝斯音量{C}检查调弦{C}并演奏几个练习音符。 | 未改动 |
| 22309 | Start by tuning the string displayed in red.  This is the fattest string on a 4 string bass. | 先调准显示为红色的琴弦。这是四弦贝斯上最粗的一根弦。 | 先调准显示为红色的琴弦。这是四弦贝斯上最粗的一根弦。 | 未改动 |
| 22372 | Syncopation describes notes that are played off the beat. | 切分音描述的是在弱拍上演奏的音符。 | 切分音描述的是在弱拍上演奏的音符。 | 未改动 |
| 22393 | Switch to Guitar? | 切换到吉他？ | 切换到吉他？ | 未改动 |
| 22402 | Guitar | 吉他 | 吉他 | 未改动 |
| 22409 | Bass is playable with a guitar if you don't own a bass. | 如果没有贝斯，可以用吉他演奏贝斯。 | 如果没有贝斯，可以用吉他演奏贝斯。 | 未改动 |
| 22454 | Modern hybrid bass amp with a classic sound. | 具有经典音色的现代混合贝斯音箱。 | 具有经典音色的现代混合贝斯音箱。 | 未改动 |
| 22459 | 1980's 2x10 bass cab. Punchy and mid-forward with an added hi frequency driver for hi frequency presence. | 1980 年代 2x10 贝斯音箱。声音有力且中频突出，额外的高频驱动器增强了高频存在感。 | 1980 年代 2x10 贝斯箱体。声音有力且中频突出，额外的高频驱动器增强了高频存在感。 | 改动 |
| 22469 | Preposterous fuzz pedal | 荒谬的模糊效果器 | 荒谬的法兹效果器 | 改动 |
| 22510 | Auto - Release | 自动 - 释放 | 自动 - 释放 | 未改动 |
| 22566 | Complete a bass event | 完成一个贝斯事件 | 完成一个贝斯事件 | 未改动 |
| 22617 | New Bass Unlocked | 解锁新贝斯 | 解锁新贝斯 | 未改动 |
| 22652 | Start Bass? | 开始贝斯？ | 开始贝斯？ | 未改动 |
| 22657 | Fingered | 指弹 | 指弹 | 未改动 |
| 22661 | Turn up your bass's volume and try again. | 调高贝斯音量，然后重试。 | 调高贝斯音量，然后重试。 | 未改动 |
| 22662 | Check your bass's connection and try again. | 检查贝斯的连接并重试。 | 检查贝斯的连接并重试。 | 未改动 |
| 22696 | Play with a pick | 使用拨片演奏 | 使用拨片演奏 | 未改动 |
| 22796 | Are you sure you want to exit the game? | 确定要退出游戏吗？ | 确定要退出游戏吗？ | 未改动 |
| 22864 | This will also change all video and audio options to their default values as if you just installed Rocksmith.  This may cause your screen resolution to change.  Some options will not be reset until you restart Rocksmith. | 这还会将所有视频和音频选项重置为默认值，就像你刚安装 Rocksmith 一样。这可能会导致你的屏幕分辨率发生变化。部分选项将在你重启 Rocksmith 后才会重置。 | 这还会将所有视频和音频选项重置为默认值，就像你刚安装 Rocksmith 一样。这可能会导致你的屏幕分辨率发生变化。部分选项将在你重启 Rocksmith 后才会重置。 | 未改动 |
| 23195 | Jam | Jam | Jam | 未改动 |
| 23392 | Crappy | 糟糕 | 糟糕 | 未改动 |
| 23523 | This is what an E chord looks like. | 这就是 E 和弦的样子。 | 这就是 E 和弦的样子。 | 未改动 |
| 23531 | If you ever want to get more in depth with anything in Rocksmith{C} just pull up the Help menu or check out the Technique Book. | 如果你想深入了解 Rocksmith 中的任何内容{C}只需调出帮助菜单或查看技巧手册。 | 如果你想深入了解 Rocksmith 中的任何内容{C}，只需调出帮助菜单或查看技巧手册。 | 改动 |
| 23564 | Here are some tips on how to use your pick to play a single string. Take a look and spend a few minutes getting used to that action. | 这里有一些关于如何使用拨片弹奏单根琴弦的技巧。请查看并花几分钟熟悉这个动作。 | 这里有一些关于如何使用拨片弹奏单根琴弦的技巧。请查看并花几分钟熟悉这个动作。 | 未改动 |
| 23680 | You overshot the bend there. This is just a tiny one{C} less than a half-step. | 你刚才推弦过头了。这只是一个很小的{C} 不到半音的推弦。 | 你刚才推弦过头了。这只是一个很小的推弦{C}，不到半音。 | 改动 |
| 23723 | Hold down the 13th fret of the B string while you bend at the 15th fret of the G string. | 按住B弦第13品，同时在G弦第15品进行推弦。 | 按住B弦第13品，同时在G弦第15品进行推弦。 | 未改动 |
| 23786 | Sounds like you missed the low E string that time. Let's try to get both notes in there. | 听起来你刚才漏掉了低音E弦。让我们试着把两个音符都弹出来。 | 听起来你刚才漏掉了低音E弦。让我们试着把两个音符都弹出来。 | 未改动 |
| 23810 | Put your 1st finger on the 1st fret of the B string{C} your 2nd finger on the 2nd fret of the D string and your 3rd finger on the 2nd fret of the G string{C} then strum. | 将食指按在 B 弦的 1 品{C} 中指按在 D 弦的 2 品，无名指按在 G 弦的 2 品{C} 然后扫弦。 | 将食指按在 B 弦的 1 品{C} 中指按在 D 弦的 2 品，无名指按在 G 弦的 2 品{C} 然后扫弦。 | 未改动 |
| 23934 | You're getting that open low E string in there. Try to play only the A and D strings{C} and mute the rest. | 你弹到了空弦的低音E弦。试着只弹A弦和D弦{C}并制音其余琴弦。 | 你弹到了空弦的低音E弦。试着只弹A弦和D弦{C}并制音其余琴弦。 | 未改动 |
| 23964 | Not getting anything... A note will only sound if your finger is directly over the metal fret wire - otherwise you'll just mute the string. | 没有声音……只有当手指直接按在金属品丝上时，音符才会发声，否则只会闷住琴弦。 | 没有声音……只有当手指直接按在金属品丝上时，音符才会发声，否则只会闷住琴弦。 | 未改动 |
| 24132 | You drive the music. The band reacts to how you play{C} so they'll match your Intensity. You can even change your key or tempo. | 由你主导音乐。乐队会根据你的演奏做出反应{C} 因此他们会匹配你的强度。你甚至可以改变调性或速度。 | 由你主导音乐。乐队会根据你的演奏做出反应{C} 因此他们会匹配你的强度。你甚至可以改变调性或速度。 | 未改动 |
| 24178 | Your hammer-on didn't catch both strings. Make sure your finger hammers onto both the G and B strings when it comes down. | 你的击弦没有同时触碰到两根弦。确保手指落下时同时敲击 G 弦和 B 弦。 | 你的击弦没有同时触碰到两根弦。确保手指落下时同时敲击 G 弦和 B 弦。 | 未改动 |
| 24198 | Master even more techniques with tons of new lessons and over a dozen new Guitarcade games. | 通过大量新教程和十余款新吉他街机游戏，掌握更多技巧。 | 通过大量新教程和十余款新吉他街机游戏，掌握更多技巧。 | 未改动 |
| 24225 | Now{C} pick a game and get playing! | 现在{C}选一首歌开始演奏吧！ | 现在{C}选一首歌开始演奏吧！ | 未改动 |
| 24240 | Don't mute that first chord. Let it keep ringing out after you hammer on those two notes. | 不要制音第一个和弦。在你击弦那两个音符后，让它继续共鸣。 | 不要制音第一个和弦。在你击弦那两个音符后，让它继续共鸣。 | 未改动 |
| 24318 | That sounded like the 17th fret. We're going for the 15th fret. | 听起来像是第17品。我们要按第15品。 | 听起来像是第17品。我们要按第15品。 | 未改动 |
| 24327 | That sounded like the 17th fret. We're going for the 19th fret. | 听起来像是第 17 品。我们要的是第 19 品。 | 听起来像是第 17 品。我们要的是第 19 品。 | 未改动 |
| 24330 | That sounded like the 21st fret. We're going for the 19th fret. | 听起来像是第21品。我们要的是第19品。 | 听起来像是第21品。我们要的是第19品。 | 未改动 |
| 24658 | Sounds like you're on the G string. This pop happens on the D string. | 听起来你在G弦上。这个拨弦动作在D弦上。 | 听起来你在G弦上。这个爆音发生在D弦上。 | 改动 |
| 24791 | There's a few key things to remember about the way Rocksmith does things. | 关于 Rocksmith 的运作方式，有几件关键的事情需要记住。 | 关于 Rocksmith 的运作方式，有几件关键的事情需要记住。 | 未改动 |
| 24803 | You just pluck the string you pre-bent{C} and then bring it back down to the regular fretted note. | 你刚刚拨动了预先推弦的琴弦{C}然后将其拉回正常的按弦音符。 | 你只需拨动预先推弦的琴弦{C}然后让它回到正常的按弦音符。 | 改动 |
| 24832 | The all-new Rocksmith 2014 Edition | 全新 Rocksmith 2014 Edition | 全新 Rocksmith 2014 Edition | 未改动 |
| 24865 | You've earned a prize!  Amazing! | 你赢得了奖励！太棒了！ | 你赢得了奖励！太棒了！ | 未改动 |
| 24879 | Here's that same idea{C} but in a different location on the guitar. | 这是同样的概念{C}但在吉他的不同位置。 | 这是同样的概念{C}但在吉他的不同位置。 | 未改动 |
| 24981 | You can mix some frethand mutes into your chord strumming to add a percussive element to your playing. | 你可以在扫弦和弦中加入一些左手制音，为你的演奏增添打击乐元素。 | 你可以在和弦扫弦中加入一些左手制音，为你的演奏增添打击乐元素。 | 改动 |
| 24995 | This sliding tremolo thing is a classic effect heard in surf rock. | 这种滑音颤音效果是冲浪摇滚中的经典音效。 | 这种滑音颤音效果是冲浪摇滚中的经典音效。 | 未改动 |
| 25061 | You can slide immediately after you hit a note{C} or you can hold it for a while and then slide. | 你可以在击中音符后立即滑音{C}或者保持一段时间后再滑音。 | 你可以在击中音符后立即滑音{C}或者保持一段时间后再滑音。 | 未改动 |
| 25083 | Palm mutes make notes shorter and a little more muffled. The musical term for playing short notes is "staccato". | 手掌制音使音符变短且略显沉闷。演奏短音符的音乐术语是“断奏”。 | 手掌制音使音符变短且略显沉闷。演奏短音符的音乐术语是“断奏”。 | 未改动 |
| 25092 | Double stops are two-note chords that are great for Comping or building Intensity in a solo. {L}{L}The Scale Notes in Session Mode make it easy to see potential double stops. Just hold down any two notes in the scale{C} and you've got a double stop! In the next Session{C} try grabbing some double stops from the Scale Shapes on the fretboard. | 双音是两个音符组成的和弦，非常适合用于伴奏或增强独奏的张力。{L}{L}即兴演奏模式中的音阶音符让你能轻松发现潜在的双音。只需按住音阶中的任意两个音符{C}你就得到了一个双音！在下一次即兴演奏中{C}试着从指板上的音阶型中抓取一些双音。 | 双音是两个音符组成的和弦，非常适合用于伴奏或增强独奏的张力。{L}{L}即兴演奏模式中的音阶音符让你能轻松发现潜在的双音。只需按住音阶中的任意两个音符{C}你就得到了一个双音！在下一次即兴演奏中{C}试着从指板上的音阶型中抓取一些双音。 | 未改动 |
| 25101 | On top of who they like{C} Session Mode instruments can be very picky about WHAT they like. The description of each instrument gives you some hints about what settings it likes the most. Equip an instrument with settings it likes to get it to sound its best. | 在它们喜欢的东西之上{C} 即兴演奏模式的乐器对它们喜欢什么非常挑剔。每种乐器的描述都会给你一些关于它最喜欢哪些设置的提示。装备它喜欢的设置，让它发挥最佳音色。 | 除了它们喜欢谁之外{C} 即兴演奏模式的乐器对它们喜欢什么非常挑剔。每种乐器的描述都会给你一些关于它最喜欢哪些设置的提示。给乐器配备它喜欢的设置，让它发挥最佳音色。 | 改动 |
| 25147 | You can use a lot of the same effects you'd use on a single string on double stops too - either on both notes or just one of them. | 你可以在双音中使用许多与单弦相同的效果——要么应用于两个音符，要么只应用于其中一个。 | 你可以在双音中使用许多与单弦相同的效果——要么应用于两个音符，要么只应用于其中一个。 | 未改动 |
| 25156 | Did you notice that other positions of the scale look pretty familiar? They should... you've played them all. The Scale Shapes you've been playing are always connected to each other all the way up and down the neck. {L}{L}More and more{C} you should think about scales as a road map that covers the whole fretboard. The more you see how scales are connected{C} the more options you have. | 你注意到音阶的其他把位看起来很熟悉吗？应该如此……你都弹过。你一直在弹奏的音阶形状在指板上从头到尾都是相互连接的。 {L}{L}越来越多地{C} 你应该把音阶看作覆盖整个指板的路线图。你越了解音阶之间的连接{C} 你的选择就越多。 | 你注意到音阶的其他把位看起来很熟悉吗？应该如此……你都弹过。你一直在弹奏的音阶形状在指板上从头到尾都是相互连接的。 {L}{L}越来越多地{C} 你应该把音阶看作覆盖整个指板的路线图。你越了解音阶之间的连接{C} 你的选择就越多。 | 未改动 |
| 25407 | For more info{C} check out the Bends Lesson. | 如需更多信息{C}请查看推弦课程。 | 如需更多信息{C}请查看推弦课程。 | 未改动 |
| 25422 | You can get to Score Attack straight from Learn a Song to quickly switch between learning and competing. | 你可以直接从学习歌曲进入得分挑战，以便在学习和竞争之间快速切换。 | 你可以直接从学习歌曲进入得分挑战，以便在学习和竞争之间快速切换。 | 未改动 |
| 25424 | A tremolo note has a wavy tail and means you should play the note repeatedly over and over. | 颤音音符带有波浪形尾部，表示应反复弹奏该音符。 | 颤音音符带有波浪形尾部，表示应反复弹奏该音符。 | 未改动 |
| 25481 | Your technique rating is based on how well you play the different guitar or bass techniques in Rocksmith. You can raise it by getting more accurate when you hit techniques. To get better at techniques{C} be sure to check out lessons and Guitarcade games. | 你的技巧评分基于你在 Rocksmith 中演奏不同吉他或贝斯技巧的熟练程度。通过更准确地演奏技巧可以提高评分。要提升技巧{C}请务必查看课程和吉他街机游戏。 | 你的技巧评分基于你在 Rocksmith 中演奏不同吉他或贝斯技巧的熟练程度。通过更准确地演奏技巧可以提高评分。要提升技巧{C}请务必查看课程和吉他街机游戏。 | 未改动 |
| 25554 | If a chord pane has notes ghosted inside{C} then it's an arpeggio.  The chord is broken up{C} but it's a lot easier to play if you hold down the chord shape. | 如果和弦面板内有幽灵音符{C}那就是分解和弦。和弦被拆分了{C}但按住和弦形状演奏会容易得多。 | 如果和弦面板内有幽灵音符{C}那就是分解和弦。和弦被拆分了{C}但按住和弦形状演奏会容易得多。 | 未改动 |
| 25632 | Strumming harder or softer to control your volume and muting your strings are important basic skills you'll need to get down. | 通过轻重不同的扫弦控制音量以及制音，是你必须掌握的重要基础技巧。 | 通过轻重不同的扫弦控制音量以及制音，是你必须掌握的重要基础技巧。 | 未改动 |
| 25688 | Try learning to play a song on your own – it’s great for your ear. | 试着独自学习演奏一首歌——这对训练你的耳朵很有帮助。 | 试着独自学习演奏一首歌——这对训练你的耳朵很有帮助。 | 未改动 |
| 25738 | Your Session Rhythm rating tells you how far you've come in making music playing rhythm guitar with your bands. Completing session Mode missions while in the Rhythm path{C} will help you maximize your Session Rhythm rating. | 你的即兴节奏评分告诉你，在与乐队一起演奏节奏吉他方面取得了多少进步。在节奏路径下完成即兴演奏模式任务{C}将有助于最大化你的即兴节奏评分。 | 你的即兴节奏评分告诉你，在与乐队一起演奏节奏吉他方面取得了多少进步。在节奏路径下完成即兴演奏模式任务{C}将有助于最大化你的即兴节奏评分。 | 未改动 |
| 25805 | Resist the urge to play with a really thin pick. They're not great for your tone. | 忍住不用极薄拨片的冲动。它们对你的音色没有帮助。 | 忍住不用极薄拨片的冲动。它们对你的音色没有帮助。 | 未改动 |
| 25818 | It's a good idea to have a quality case{C} so when you need to move your instrument around{C} it's well-protected. | 拥有一个高质量的琴盒是个好主意{C} 这样当你需要移动乐器时{C} 它能得到很好的保护。 | 拥有一个高质量的琴盒是个好主意{C} 这样当你需要移动乐器时{C} 它能得到很好的保护。 | 未改动 |
| 25957 | Let's take your skills out for a spin and see how many you nail in one playthrough. | 让我们试试你的技巧，看看在一次演奏中能完美完成多少。 | 让我们试试你的技巧，看看在一次演奏中能完美完成多少。 | 未改动 |
| 26157 | Play around with different tunings. It can be a fun way to open up your ears and break ingrained bad habits. | 尝试不同的调弦。这是一种开阔听觉并打破固有坏习惯的有趣方式。 | 尝试不同的调弦。这是一种开阔听觉并打破固有坏习惯的有趣方式。 | 未改动 |
| 26170 | A whole step is equivalent to the interval of a Major second. A half-step is equivalent to a minor second. | 全音等同于大二度音程。半音等同于小二度音程。 | 全音等同于大二度音程。半音等同于小二度音程。 | 未改动 |
| 26233 | Turn the "auto-mode" to "OFF" and use the "Pedal" control in a wah effect to move the wah filter up and down manually. | 将“自动模式”设为“关”，并使用哇音效果中的“踏板”控制手动上下移动哇音滤波器。 | 将“自动模式”设为“关”，并使用哇音效果中的“踏板”控制手动上下移动哇音滤波器。 | 未改动 |
| 26236 | Use the Studio reverb or studio EQ to add the finishing touches to a good tone. | 使用录音室混响或录音室均衡器，为良好的音色增添最后的修饰。 | 使用录音室混响或录音室均衡器，为良好的音色增添最后的修饰。 | 未改动 |
| 26259 | Then{C} check which peg matches that string. | 然后{C}检查哪个弦钮对应这根琴弦。 | 然后{C}检查哪个弦钮对应这根琴弦。 | 未改动 |
| 26411 | Superb! | 太棒了！ | 太棒了！ | 未改动 |
| 26486 | While in Auto{C} Rocksmith will always choose the Authentic Tone for what you are playing{C} BUT you can switch to any Tone at any time using the Tone Stick. Let's assign a Tone to the Tone Stick now. | 在自动模式下{C}Rocksmith 总是为你演奏的内容选择真实音色{C}但你随时可以使用音色条切换到任何音色。让我们现在为音色条分配一个音色。 | 在自动模式下{C}Rocksmith 总是为你演奏的内容选择真实音色{C}但你随时可以使用音色条切换到任何音色。让我们现在为音色条分配一个音色。 | 未改动 |
| 26568 | When you play with a pick{C} it's good to get in the habit of Alternate picking{C} where your pick always alternates between going down on downbeats and up on upbeats. | 当你使用拨片演奏时{C}养成交替拨弦的习惯是很好的{C}即拨片始终在强拍向下、弱拍向上之间交替。 | 当你使用拨片演奏时{C}养成交替拨弦的习惯是很好的{C}即拨片始终在强拍向下、弱拍向上之间交替。 | 未改动 |
| 26592 | Continue your Rocksmith experience on the go{C} with Rocksmith 2014 mobile. | 随时随地继续你的 Rocksmith 体验{C}使用移动版 Rocksmith 2014。 | 随时随地继续你的 Rocksmith 体验{C}使用移动版 Rocksmith 2014。 | 未改动 |
| 26605 | Rocksmith 2014 | Rocksmith 2014 | Rocksmith 2014 | 未改动 |
| 26636 | G♭ | G♭ | G♭ | 未改动 |
| 26641 | D | D | D | 未改动 |
| 26644 | G | G | G | 未改动 |
| 26662 | Add the Session Drums to an Instrument Slot. | 将即兴鼓组添加到乐器槽位。 | 将即兴鼓组添加到乐器槽位。 | 未改动 |
| 26685 | TIMING IS EVERYTHING | 时机就是一切 | 时机就是一切 | 未改动 |
| 26815 | Play with the [1] Band. | 与[1]乐队一起弹奏。 | 与[1]乐队一起弹奏。 | 未改动 |
| 26833 | EMBRACING OUR DIFFERENCES | EMBRACING OUR DIFFERENCES | EMBRACING OUR DIFFERENCES | 未改动 |
| 26834 | Load the [1] Band. | 加载 [1] 乐队。 | 加载 [1] 乐队。 | 未改动 |
| 26853 | Play with Complexity set to Progressive. | 将难度设为渐进式进行演奏。 | 将难度设为渐进式进行演奏。 | 未改动 |
| 26869 | Learn a Scale Shape: Phrygian Dominant. | 学习音阶形态：弗里吉亚属音阶。 | 学习音阶形态：弗里吉亚属音阶。 | 未改动 |
| 26874 | Learn a Scale Shape: Harmonic Minor. | 学习音阶形态：和声小调。 | 学习音阶形态：和声小调。 | 未改动 |
| 26887 | Session for 30 minutes. | 即兴演奏 30 分钟。 | 即兴演奏 30 分钟。 | 未改动 |
| 26928 | ON REPEAT | ON REPEAT | ON REPEAT | 未改动 |
| 26938 | THE HIGH NOTE | THE HIGH NOTE | THE HIGH NOTE | 未改动 |
| 26968 | LOW TOLERANCE | 低容差 | 低容差 | 未改动 |
| 26984 | Successfully hit a chord. | 成功弹奏了一个和弦。 | 成功弹奏了一个和弦。 | 未改动 |
| 26990 | Clear a Score Attack song (Medium). | 通关一首得分挑战歌曲（中等难度）。 | 通关一首得分挑战歌曲（中等难度）。 | 未改动 |
| 27017 | WELL-BALANCED | 平衡良好 | 平衡良好 | 未改动 |
| 27025 | FREE FORM | 自由形式 | 自由形式 | 未改动 |
| 27031 | SOMETHING TO GAIN | SOMETHING TO GAIN | SOMETHING TO GAIN | 未改动 |
| 27133 | Cm7(♭5) | Cm7(♭5) | Cm7(♭5) | 未改动 |
| 27136 | Csus2 | Csus2 | Csus2 | 未改动 |
| 27145 | Cartridge Kit | Cartridge Kit | Cartridge Kit | 未改动 |
| 27162 | Studio Classic | 经典录音室 | 经典录音室 | 未改动 |
| 27194 | Synth Percussion | 合成打击乐 | 合成打击乐 | 未改动 |
| 27217 | SYNTH BASS | 合成贝斯 | 合成贝斯 | 未改动 |
| 27289 | Bm | Bm | Bm | 未改动 |
| 27302 | Dm7 | Dm7 | Dm7 | 未改动 |
| 27336 | A♭m7(♭5) | A♭m7(♭5) | A♭m7(♭5) | 未改动 |
| 27340 | A♭5 | A♭5 | A♭5 | 未改动 |
| 27345 | D♭7 | D♭7 | D♭7 | 未改动 |
| 27441 | Successfully hit a double stop. | 成功演奏了一个双音。 | 成功演奏了一个双音。 | 未改动 |
| 27489 | SOLIDBODY 7THS | SOLIDBODY 7THS | SOLIDBODY 7THS | 未改动 |
| 27528, 28994 | TOY PIANO | 玩具钢琴 | 玩具钢琴 | 未改动 |
| 27537 | Trapezoid | 梯形 | 梯形 | 未改动 |
| 27587 | Gibson® Dickey Betts SG | Gibson® Dickey Betts SG | Gibson® Dickey Betts SG | 未改动 |
| 27689 | Score at least [1] points in Star Chords | 至少得分 [1] 分（Star Chords） | 至少得分 [1] 分（Star Chords） | 未改动 |
| 27699 | Score [1] points in Temple of Bends | 得分 [1] 分于 Temple of Bends | 在 Temple of Bends 中获得 [1] 分。 | 改动 |
| 27722 | Ernie Ball’s Long Streak Special | Ernie Ball 连胜特别版 | Ernie Ball 连胜特别版 | 未改动 |
| 27794 | Accents look like this: | 重音符号如下所示： | 重音符号如下所示： | 未改动 |
| 27802, 32647 | Perfect! | 完美！ | 完美！ | 未改动 |
| 27928 | Time to dive in. | 是时候深入练习了。 | 是时候深入练习了。 | 未改动 |
| 27930 | Play it now. | 现在弹奏。 | 现在弹奏。 | 未改动 |
| 28024 | Now a little faster. | 现在稍微快一点。 | 现在稍微快一点。 | 未改动 |
| 28243 | Try it now. | 现在就试试。 | 现在就试试。 | 未改动 |
| 28265 | Get ready. | 准备就绪。 | 准备好。 | 改动 |
| 28269 | Get ready to try{C} we'll bring you in. | 准备好尝试{C}，我们将带你入门。 | 准备好尝试{C}，我们将带你入门。 | 未改动 |
| 28365 | Let's play it at full speed now. | 现在让我们以全速演奏。 | 现在让我们以全速演奏。 | 未改动 |
| 28663 | Masterful! | 大师级！ | 大师级！ | 未改动 |
| 28928 | SESSION DRUMS | SESSION DRUMS | 合奏鼓组 | 改动 |
| 28977 | TREMOLO PAD | 颤音踏板 | 颤音垫 | 改动 |
| 29078 | Raise your Session Bass rating. | 提高你的即兴贝斯等级。 | 提高你的即兴贝斯等级。 | 未改动 |
| 29103 | SCORE CORE | 得分核心 | 得分核心 | 未改动 |
| 29154 | HOT PURSUIT | HOT PURSUIT | HOT PURSUIT | 未改动 |
| 29183 | NINJA STAR | NINJA STAR | NINJA STAR | 未改动 |
| 29184 | CAR CHASE | 汽车追逐 | 汽车追逐 | 未改动 |
| 29239 | PICK AND CHOOSE | 自选 | 自选 | 未改动 |
| 29333 | VERY GOOD REHEARSAL! | 排练非常棒！ | 排练非常棒！ | 未改动 |
| 30072 | PHRYGIAN FUNK | 弗里吉亚放克 | 弗里吉亚放克 | 未改动 |
| 30109 | SIMPLE SLOW JAM | 简约慢速即兴 | 简约慢速即兴 | 未改动 |
| 30130 | VINTAGE ROCK | 复古摇滚 | 复古摇滚 | 未改动 |
| 30145 | JAZZ BAR | JAZZ BAR | 爵士酒吧 | 改动 |
| 30155 | NU METAL | 新金属 | 新金属 | 未改动 |
| 30160 | DEATH METAL | 死亡金属 | 死亡金属 | 未改动 |
| 30162 | SPEED METAL | 速度金属 | 速度金属 | 未改动 |
| 30184 | FUNK FUSION | 放克融合 | 放克融合 | 未改动 |
| 30221 | MODERN BLUES | 现代蓝调 | 现代蓝调 | 未改动 |
| 30225 | CAMPFIRE BLUES | CAMPFIRE BLUES | CAMPFIRE BLUES | 未改动 |
| 30237 | BASEMENT CARTRIDGE | 地下室卡带 | 地下室卡带 | 未改动 |
| 30264 | CLASSIC FUNK ROCK | 经典放克摇滚 | 经典放克摇滚 | 未改动 |
| 30286 | ¡OLÉ! | ¡OLÉ! | ¡OLÉ! | 未改动 |
| 30325 | THUNK DRUNK | THUNK DRUNK | THUNK DRUNK | 未改动 |
| 30381 | HG100 | HG100 | HG100 | 未改动 |
| 30401 | Gibson® GA-79 RVT "Dual" | Gibson® GA-79 RVT "Dual" | Gibson® GA-79 RVT "Dual" | 未改动 |
| 30406 | A 1962 classic 15-watt combo. | 一款 1962 年经典的 15 瓦组合音箱。 | 一款 1962 年经典的 15 瓦组合音箱。 | 未改动 |
| 30450 | CSS300B | CSS300B | CSS300B | 未改动 |
| 30467 | Adds a standard chorus effect. | 添加标准合唱效果。 | 添加标准合唱效果。 | 未改动 |
| 30509 | Adds a 5-band graphic EQ for basic tone manipulation. | 添加一个 5 段图形均衡器，用于基本音色调节。 | 添加一个 5 段图形均衡器，用于基本音色调节。 | 未改动 |
| 30550 | Germanium Drive | 锗驱动 | 锗驱动 | 未改动 |
| 30551 | Adds classic smooth overdrive. | 添加经典顺滑的过载效果。 | 添加经典顺滑的过载效果。 | 未改动 |
| 30555 | An '80s-style overdrive pedal. | 一款80年代风格的过载效果器。 | 一款80年代风格的过载效果器。 | 未改动 |
| 30574 | Tube Spring Reverb | 电子管弹簧混响 | 电子管弹簧混响 | 未改动 |
| 30618 | Bass Enbiggenator | Bass Enbiggenator | Bass Enbiggenator | 未改动 |
| 30632 | Studio Compressor | 录音室压缩器 | 录音室压缩器 | 未改动 |
| 30658 | Orange OBC115 Bass Cab | Orange OBC115 贝斯音箱 | Orange OBC115 贝斯箱体 | 改动 |
| 30751 | A mid-sized PA system. | 中型扩声系统。 | 中型扩声系统。 | 未改动 |
| 30854 | HG180 | HG180 | HG180 | 未改动 |
| 30968 | Viscosity Echo | 粘稠回声 | 粘稠回声 | 未改动 |
| 30972 | Acoustic Emulator | 原声模拟器 | 原声模拟器 | 未改动 |
| 31026 | Phaser | 相位器 | 相位器 | 未改动 |
| 31245 | A high-gain boutique style amp. | 一款高增益精品风格音箱。 | 一款高增益精品风格音箱。 | 未改动 |
| 31264 | EN30 | EN30 | EN30 | 未改动 |
| 31309 | A classic Orange head with FAC and HF drive control. | 一款带有FAC和高频驱动控制的经典Orange头。 | 一款带有FAC和高频驱动控制的经典Orange音箱头。 | 改动 |
| 31313 | "THE" classic rock distortion sound. | “THE”经典摇滚失真音色。 | “THE”经典摇滚失真音色。 | 未改动 |
| 31321 | A modern Marshall head with a very wide range of tones. | 现代 Marshall 音箱头，拥有极宽的音色范围。 | 现代 Marshall 音箱头，拥有极宽的音色范围。 | 未改动 |
| 31325 | A straightforward Marshall head with modern gain. | 一款具有现代增益的简洁 Marshall 箱头。 | 一款具有现代增益的简洁 Marshall 箱头。 | 未改动 |
| 31371 | Add a standard distortion effect. | 添加标准失真效果。 | 添加标准失真效果。 | 未改动 |
| 31402 | 8-BAND GRAPHIC EQ | 8段图形均衡器 | 8段图形均衡器 | 未改动 |
| 31411 | Adds a synth-style envelope filter. | 添加合成器风格的包络滤波器。 | 添加合成器风格的包络滤波器。 | 未改动 |
| 31440 | CUSTOM DRIVE | CUSTOM DRIVE | CUSTOM DRIVE | 未改动 |
| 31476 | AMP VIBE | 音箱氛围 | 音箱氛围 | 未改动 |
| 31492 | BASS FILTER DELAY | 贝斯滤波延迟 | 贝斯滤波延迟 | 未改动 |
| 31517 | Adds a sub-octave pitch-shift voiced for bass. | 添加专为贝斯调音的低八度移调效果。 | 添加专为贝斯调校的低八度移调效果。 | 改动 |
| 31566 | CH210BC | CH210BC | CH210BC | 未改动 |
| 31592 | GA-8 DISCOVERER CAB | GA-8 DISCOVERER CAB | GA-8 DISCOVERER CAB | 未改动 |
| 31596 | ORANGE PPC212OB | ORANGE PPC212OB | ORANGE PPC212OB | 未改动 |
| 31625 | A rare vintage 2x15 cab. | 一款稀有的复古2x15音箱。 | 一款稀有的复古2x15箱体。 | 改动 |
| 31633 | A UK-style 4x12. | 一款英式4x12音箱。 | 一款英式4x12音箱。 | 未改动 |
| 31635 | A classic UK style 4x12. | 一款经典英式 4x12 音箱。 | 一款经典英式 4x12 音箱。 | 未改动 |
| 31656 | BTQ-1120C | BTQ-1120C | BTQ-1120C | 未改动 |
| 31657 | A boutique open-back 1x12 cab. | 一款精品开放式背板 1x12 音箱。 | 一款精品开放式背板 1x12 箱体。 | 改动 |
| 31760 | Remove your capo prior to tuning. | 调弦前请取下变调夹。 | 调弦前请取下变调夹。 | 未改动 |
| 31815 | If you’re currently missing a supported instrument{C} the Rocksmith Real Tone Cable{C} or both{C} you can still check out the game. You can return to this introduction by visiting the Lessons. | 如果你目前缺少受支持的乐器{C}Rocksmith Real Tone Cable{C}或两者都缺{C}你仍然可以体验游戏。你可以通过访问课程返回此介绍。 | 如果你目前缺少受支持的乐器{C}Rocksmith Real Tone Cable{C}或两者都缺{C}你仍然可以体验游戏。你可以通过访问课程返回此介绍。 | 未改动 |
| 31824 | Help! I Don’t Have a Cable and/or Instrument. | 求助！我没有线缆和/或乐器。 | 求助！我没有线缆和/或乐器。 | 未改动 |
| 31896 | Play with your Root in B. | 将根音设为 B 进行演奏。 | 将根音设为 B 进行演奏。 | 未改动 |
| 31968 | 9. Master | 9. 大师 | 9. 大师 | 未改动 |
| 32022 | Shoot 20 rainbow ducks. | 射击 20 只彩虹鸭子。 | 射击 20 只彩虹鸭子。 | 未改动 |
| 32059 | Jump only when leaping a hurdle in a single game. | 仅在单次游戏中跳跃跨越障碍时跳跃。 | 仅在单次游戏中跳跃跨越障碍时跳跃。 | 未改动 |
| 32090 | Leap a hurdle and collect a bolt at the same time [1] times. | 跳过障碍并同时收集螺栓 [1] 次。 | 跳过障碍并同时收集螺栓 [1] 次。 | 未改动 |
| 32101 | Collect [1] banana chains in a row. | 连续收集[1]串香蕉。 | 连续收集[1]串香蕉。 | 未改动 |
| 32131 | Skip a platform by jumping to one above it. | 通过跳到其上方的平台来跳过某个平台。 | 通过跳到其上方的平台来跳过某个平台。 | 未改动 |
| 32154 | Destroy [1] zap platforms with the shredder fan without jumping on them. | 摧毁 [1] 个电击平台，使用粉碎风扇且不要跳上去。 | 用粉碎风扇摧毁 [1] 个电击平台，且不要跳到这些平台上。 | 改动 |
| 32189 | Steal [1] jewels from giant treasure masks in a single game. | 偷取 [1] 颗宝石，从巨型宝藏面具中，在一局游戏内。 | 在一局游戏中，从巨型宝藏面具中偷取 [1] 颗宝石。 | 改动 |
| 32231 | Play a slide on every color of string. | 在所有颜色的琴弦上演奏滑音。 | 在所有颜色的琴弦上演奏滑音。 | 未改动 |
| 32260 | Slice [1] yellow ghosts. | Slice [1]黄色幽灵。 | 切 [1] 黄色幽灵。 | 改动 |
| 32276 | Play 5 correct notes in a row. | 连续演奏 5 个正确的音符。 | 连续演奏 5 个正确的音符。 | 未改动 |
| 32282 | Play 2 correct notes in quick succession. | 快速连续弹奏2个正确的音符。 | 快速连续弹奏2个正确的音符。 | 未改动 |
| 32311 | Take [1] off-ramps up the fretboard. | 在指板上[1]使用离弦技巧。 | 在指板上做出 [1] 个上行滑音。 | 改动 |
| 32351 | Destroy a mini-ship without getting hit. | 在不被击中的情况下摧毁一艘小型飞船。 | 在不被击中的情况下摧毁一艘小型飞船。 | 未改动 |
| 32367 | Destroy [1] enemy ships just before they attack. | 摧毁 [1] 艘敌舰，就在它们发动攻击之前。 | 摧毁 [1] 艘敌舰，就在它们发动攻击之前。 | 未改动 |
| 32517 | Play the matching chord repeatedly to destroy runestones and absorb the chord's power. | 反复演奏匹配的和弦以摧毁符文石并吸收和弦的力量。 | 反复演奏匹配的和弦以摧毁符文石并吸收和弦的力量。 | 未改动 |
| 32536 | Play notes to fill your special meter. | 弹奏音符以填充特殊计量表。 | 弹奏音符以填充特殊计量表。 | 未改动 |
| 32563 | Not launching your ninja? Check your fret fingers. | 忍者没启动？检查一下你的按品手指。 | 忍者没启动？检查一下你的按品手指。 | 未改动 |
| 32664 | Underslide! | 下滑音！ | 下滑音！ | 未改动 |
| 32675 | Quick! | 快！ | 快！ | 未改动 |
| 32684 | Overbend! | 过载！ | 推弦过度！ | 改动 |
| 32720 | B5 | B5 | B5 | 未改动 |
| 32760 | Gm9 | Gm9 | Gm9 | 未改动 |
| 32827 | Ha ha ha! The power belongs to ME! | 哈哈哈！力量属于我！ | 哈哈哈！力量属于我！ | 未改动 |
| 32894 | Why?!?!?!? | 为什么？！ | 为什么？！ | 未改动 |
| 32919 | Finally! You see{C} this feels awesome. Go me. | 终于！你看{C} 这种感觉太棒了。我做到了。 | 终于！你看{C} 这种感觉太棒了。我真棒。 | 改动 |
| 33356 | Adding More Techniques | 添加更多技巧 | 添加更多技巧 | 未改动 |
| 33430 | Syncopation 201B | 切分音 201B | 切分音 201B | 未改动 |
| 33467 | Bass 102 | 贝斯 102 | 贝斯 102 | 未改动 |
| 33652 | Learn about power chords{C} one of the cornerstones of the rock guitar sound. | 了解强力和弦{C}，它是摇滚吉他声音的基石之一。 | 了解强力和弦{C}，它是摇滚吉他声音的基石之一。 | 未改动 |
| 33668 | Learn how to combine hammer-ons and pull-offs with each other and with other techniques like slides and double stops to get more interesting effects. | 学习如何将击弦和勾弦与其他技巧如滑音和双音结合，以获得更丰富的效果。 | 学习如何将击弦和勾弦彼此结合，再与滑音和双音等其他技巧结合，以获得更有趣的效果。 | 改动 |
| 33731 | Expand your bass vocabulary with a practice track focused on a classic Rock and Roll bass pattern. | 通过专注于经典摇滚贝斯模式的练习曲目，扩展你的贝斯词汇量。 | 通过专注于经典摇滚贝斯模式的练习曲目，扩展你的贝斯词汇量。 | 未改动 |
| 33874 | You're getting pretty solid at playing this song. Why not challenge yourself to level it up? When you do{C} the amount of the full song you'll see when you play will increase. | 你演奏这首歌已经相当扎实了。为什么不挑战自己提升等级呢？当你这样做时{C}你演奏时看到的完整歌曲部分会增加。 | 你演奏这首歌已经相当扎实了。为什么不挑战自己提升等级呢？当你这样做时{C}你演奏时看到的完整歌曲内容会增加。 | 改动 |
| 34029 | Manually switch tones during a song. | 在歌曲演奏期间手动切换音色。 | 在歌曲演奏期间手动切换音色。 | 未改动 |
| 34096 | Play a Special Topics Lesson. | 学习一节专题课程。 | 学习一节专题课程。 | 未改动 |
| 34107 | Successfully hit an octave. | 成功完成八度音程。 | 成功奏出八度音。 | 改动 |
| 34117 | Successfully hit 4 sixths. | 成功演奏了 4 个六度音程。 | 成功演奏了 4 个六度音程。 | 未改动 |
| 34203 | double stops | 双音 | 双音 | 未改动 |
| 34210 | palm mute double stops | 手掌闷音双音 | 手掌闷音双音 | 未改动 |
| 34229 | Slap Fret Hand Mutes | Slap 左手闷音 | Slap 左手制音 | 改动 |
| 34284 | Breakdown | 分解段落 | 分解段落 | 未改动 |
| 34305 | Tapping | 点弦 | 点弦 | 未改动 |
| 34492 | Arpeggios | 琶音 | 琶音 | 未改动 |
| 34499 | An Intro to Hammer-ons and Pull-offs | 击弦与勾弦入门 | 击弦与勾弦入门 | 未改动 |
| 34526 | Unpitched Slide | 无音高滑音 | 无音高滑音 | 未改动 |
| 34564 | Maintenance | 维护 | 维护 | 未改动 |
| 34683 | Set to [1] | 已设为 [1] | 已设为 [1] | 未改动 |
| 34748 | Please provide the following information to create your account. | 请提供以下信息以创建您的账户。 | 请提供以下信息以创建你的账户。 | 改动 |
| 34756 | PLAY TIME | 游玩时长 | 游玩时长 | 未改动 |
| 34760 | 3. "In Tune" Marker | 3. “音准”标记 | 3. “音准”标记 | 未改动 |
| 34785 | SESSION GAMEPLAY DIAGRAM | 即兴演奏示意图 | 即兴演奏示意图 | 未改动 |
| 34804 | Up/Down/Left/Right Cursor = D-pad | 上/下/左/右光标 = 方向键 | 上/下/左/右光标 = 方向键 | 未改动 |
| 34872 | Two Rocksmith Real Tone Cables have been detected. We don’t know which one you’re using. Disconnect one or go to Multiplayer to use both. | 检测到两根 Rocksmith Real Tone Cable。我们不知道您正在使用哪一根。请断开其中一根，或前往多人模式以同时使用两根。 | 检测到两根 Rocksmith Real Tone Cable。我们不知道你正在使用哪一根。请断开其中一根，或前往多人模式以同时使用两根。 | 改动 |
| 34880 | RESTART PRACTICE TRACK | 重新开始练习曲目 | 重新开始练习曲目 | 未改动 |
| 34900 | Both passwords are not the same. | 两次输入的密码不一致。 | 两次输入的密码不一致。 | 未改动 |
| 34912 | Sign in to Xbox Live to access online features of this title. | 登录 Xbox Live 以访问此游戏的在线功能。 | 登录 Xbox Live 以访问此游戏的在线功能。 | 未改动 |
| 34952 | Perfect Lane Changes | 完美变道 | 完美变道 | 未改动 |
| 35028 | B | B | B | 未改动 |
| 35048 | Streak Broken! | 连击中断！ | 连击中断！ | 未改动 |
| 35088 | Streak{B}Challenge | 连击{B}挑战 | 连击{B}挑战 | 未改动 |
| 35185 | Crash cop cars for massive points. | 撞毁警车以获得大量分数。 | 撞毁警车以获得大量分数。 | 未改动 |
| 35188 | Slice ghosts for massive points. | 切幽灵获得大量分数。 | 切幽灵获得大量分数。 | 未改动 |
| 35298 | Consonance / Consonant | 协和 / 协和音 | 协和 / 协和音 | 未改动 |
| 35319 | This is when you improvise over Chord Changes that require you to borrow from other scales to remain Consonant. In Session Mode{C} the harder Complexities change Scale Notes to follow the Chord Changes. | 这是在和弦变化上即兴演奏，要求你借用其他音阶以保持协和。在即兴演奏模式中{C} 更复杂的难度会改变音阶音符以跟随和弦变化。 | 这是在和弦变化上即兴演奏，要求你借用其他音阶以保持协和。在即兴演奏模式中{C} 更复杂的难度会改变音阶音符以跟随和弦变化。 | 未改动 |
| 35396 | Funk | 放克 | 放克 | 未改动 |
| 35403 | Bebop | Bebop | Bebop | 未改动 |
| 35420 | Electro | 电子 | 电子 | 未改动 |
| 35460 | Pentatonic Minor Metal | Pentatonic Minor Metal | Pentatonic Minor Metal | 未改动 |
| 35474 | Lydian electronic | 利底亚电子 | 利底亚电子 | 未改动 |
| 35488 | Phrygian Dominant Jam | 弗里吉亚属调即兴 | 弗里吉亚属调即兴 | 未改动 |
| 35542 | Complex Funk | 复杂放克 | 复杂放克 | 未改动 |
| 35547 | Chill Rock | 轻松摇滚 | 轻松摇滚 | 未改动 |
| 35580 | Experimental Metal | 实验金属 | 实验金属 | 未改动 |
| 35586 | Studio Metal | Studio Metal | Studio Metal | 未改动 |
| 35669 | Alternative Rock | 另类摇滚 | 另类摇滚 | 未改动 |
| 35734 | Processed | 已处理 | 已处理 | 未改动 |
| 35832 | Play the Chord! | 弹奏和弦！ | 弹奏和弦！ | 未改动 |
| 35864 | Scales | 音阶 | 音阶 | 未改动 |
| 36012 | 3. If your HDTV does not have a PC or Game Mode{C} access your HDTV’s Options menu{C} disable image scaling{C} and turn off all processing effects. | 3. 如果您的 HDTV 没有 PC 或游戏模式{C} 请进入 HDTV 的选项菜单{C} 关闭图像缩放{C} 并关闭所有处理效果。 | 3. 如果你的 HDTV 没有 PC 或游戏模式{C} 请进入 HDTV 的选项菜单{C} 关闭图像缩放{C} 并关闭所有处理效果。 | 改动 |
| 36047 | RESULTS | 结果 | 结果 | 未改动 |
| 36091 | To Change Scales{C} Press [1] | 要更改音阶{C} 按下 [1] | 要更改音阶{C} 按下 [1] | 未改动 |
| 36092 | Master Mode Unlocked! | 大师模式已解锁！ | 大师模式已解锁！ | 未改动 |
| 36112 | Please exit or complete your active gameplay and then change your Path in a menu area. | 请退出或完成当前游戏，然后在菜单区域更改你的 Path。 | 请退出或完成当前游戏，然后在菜单区域更改你的路径。 | 改动 |
| 36121 | SCREEN KEYS | SCREEN KEYS | 屏幕按键 | 改动 |
| 36482 | BAREBONES ROCK | 极简摇滚 | 极简摇滚 | 未改动 |
| 36760 | PLAYSTATION®4 SYSTEM | PlayStation®4 系统 | PlayStation®4 系统 | 未改动 |
| 36861 | TEXT TOO LONG | 文本过长 | 文本过长 | 未改动 |
| 36906 | RESTORE DIFFICULTY DEFAULTS | 恢复难度默认设置 | 恢复难度默认设置 | 未改动 |
| 36909 | Are you sure you want to reset all Difficulty Settings back to their defaults? | 确定要将所有难度设置重置为默认值吗？ | 确定要将所有难度设置重置为默认值吗？ | 未改动 |
| 36936 | NORMAL | 普通 | 普通 | 未改动 |
| 37079 | EXIT | 退出 | 退出 | 未改动 |
| 37082 | Skip Tuner | 跳过调音器 | 跳过调音器 | 未改动 |
| 37150 | Makes the in-game bass headstock match yours | 使游戏内的贝斯琴头与你的相符 | 使游戏内的贝斯琴头与你的相符 | 未改动 |
| 37196 | Your input volume seems low{C} please double check your volume and tone knobs{C} and follow the calibration checklist. | 你的输入音量似乎偏低{C}请再次检查你的音量和音色旋钮{C}并遵循校准检查清单。 | 你的输入音量似乎偏低{C}请再次检查你的音量和音色旋钮{C}并遵循校准检查清单。 | 未改动 |
| 37206 | Customer Support | 客户支持 | 客户支持 | 未改动 |
| 37208 | EULA | EULA | EULA | 未改动 |
| 37263 | RESUME PRACTICE | 继续练习 | 继续练习 | 未改动 |
| 37314 | Replay the Intro Sequence | 重播开场序列 | 重播开场序列 | 未改动 |
| 37343 | DIFFICULTY | 难度 | 难度 | 未改动 |

## 4. 请输出（建议格式）

```
## 审阅结论
### A. 逐条判定（可选，可只列需要改的）
- ids: [...], 采纳: 现译/DS/重译, 最终文本: "...", 理由: "..."
### B. 归纳规则（重点）
- 规则1: ...
  - 证据: ids [...]
### C. 建议落到程序里的修复（如全局替换、术语表、prompt 修改）
```

## 5. 附加材料
- `data/proofread_sample500.json`：500 条 id 的 DS 最终文本（含未改动）
- `data/proofread_sample500_changes.json`：仅改动明细（id -> {source,before,after}）
- `data/translations_remaining.json`：全部现译
- `data/proofread_manual.json`：已人工锁定的最终译文（合并时优先级最高）
