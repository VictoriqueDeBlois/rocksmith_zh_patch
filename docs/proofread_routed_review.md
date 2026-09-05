# qwen 分类校对全量改动清单（723 条，供复核）

> 给另一模型/Pro 审阅：逐条判定 采纳(改为 revised)/保留(original)/重译，并归纳规则。只读，勿改数据。
> 硬约束：占位符不可动；简体；无半角逗号/换行；品牌/型号保留英文；音色名不回英文；玩家用“你”。
> 已落地不要当新问题：profile=玩家档案、cab=箱体、联排、左手制音、原曲音色、您→你(代词规则)。

统计：共 723 条；按分类 A=104 B=213 C=114 D=83 E=152 F=21 G=36
需重点复核标记(理由缺失/含‘被返回’)：69 条 -> ids: 5974, 6234, 6689, 6822, 6923, 7323, 7444, 7545, 7624, 7779, 17414, 18989, 19305, 19306, 19307, 19351, 20982, 21051, 21643, 22461, 22467, 23521, 26735, 27077, 27109, 27497, 28379, 29346, 30390, 30451, 30455, 30661, 30679, 30683, 30685, 30700, 30710, 30712, 30725, 30729, 30739, 30765, 31287, 31555, 31559, 31561, 31569, 31573, 31580, 31581, 31586, 31595, 31603, 31775, 31878, 32197, 32204, 32206, 32314, 32394

## 明细（按分类分组）

### 桶 A（104）

| id | source | original | revised | 分类 | reason |
|---|---|---|---|---|---|
| 6773 | DON'T ASK ME AGAIN | DON'T ASK ME AGAIN | 不再询问 | A | 规则18要求全大写普通标题需译为中文，原译未翻译 |
| 6774 | DON'T ASK ME AGAIN | DON'T ASK ME AGAIN | 不再询问 | A | 规则18要求全大写普通标题需译为中文，原译未翻译 |
| 6779 | DON'T ASK ME AGAIN | DON'T ASK ME AGAIN | 不再询问 | A | 规则18要求全大写普通标题需译为中文，原译保留英文属于漏译。 |
| 7430 | TILTING IN PROGRESS | TILTING IN PROGRESS | 倾斜中 | A | 全大写普通标题需译中文，TILTING IN PROGRESS 意为倾斜进行中 |
| 7435 | TILTING IN PROGRESS | TILTING IN PROGRESS | 倾斜进行中 | A | 全大写普通标题需译为中文，原译保留英文不符合规则18 |
| 7624 | Saving… | 正在保存… | 正在保存…… | A | 模型未提供理由，需复核 |
| 13550 | Speeding up again... | 正在加速... | 正在加速…… | A | 根据规则20，中文省略号应使用“……”而非半角“...”。 |
| 17672 | [1]-SONG EVENT AT [2] | [1]- 在 举办歌曲活动 [2] | [1]- 在 [2] 举办歌曲活动 | A | 原译“在 举办歌曲活动 [2]”语序混乱且占位符位置错误，[2] 应为地点，应置于“在”之后。 |
| 17687 | Mixed Event | 混合事件 | 混合活动 | A | 根据规则13及术语表，event(活动)应译为活动，而非事件 |
| 17733 | Event Complete! | 事件完成！ | 活动完成！ | A | 根据已落地术语，event(活动) 应译为活动，而非事件 |
| 17735 | Completed Event | 已完成事件 | 已完成活动 | A | 根据规则13及已落地术语，event(活动)应译为活动，而非事件 |
| 17743 | Event Failed | 事件失败 | 活动失败 | A | 根据已落地术语，event(活动)=活动，因此 Event Failed 应译为“活动失败”而非“事件失败”。 |
| 17991 | Event Qualify | 事件资格 | 活动资格 | A | Event 在 Rocksmith 语境下指游戏活动，应译为“活动”而非“事件” |
| 17995 | Play Options | 玩 Options 模式。 | 播放选项 | A | Play Options 是菜单按钮，应译为“播放选项”或“游戏选项”，原译“玩 Options 模式”将 UI 标签误译为动作指令且保留英文 |
| 18172 | Palm{L}Mute{L}Missed! | 手掌{L}护弦{L}失误！ | 手掌{L}制音{L}失误！ | A | 术语规定 palm mute 统一译为手掌制音，现译护弦错误 |
| 19078 | Bridge | 桥段 | 琴桥 | A | Bridge 在乐器语境下指琴桥，而非音乐结构中的桥段 |
| 19351 | DUCKS | DUCKS | 鸭子 | A | 模型未提供理由，需复核 |
| 21051 | Change | 改变 | 更改 | A | 模型未提供理由，需复核 |
| 21094 | Mode | 调式 | 模式 | A | 此处 Mode 指游戏设置或操作模式（如自动模式），而非音乐理论中的调式（Key/Mode），译为“调式”属于语境错误。 |
| 21176 | PRESS START | PRESS START | 按开始键 | A | 规则18要求全大写普通标题需译为中文，PRESS START 是通用操作指令而非品牌专名 |
| 21218 | Authentic Tones: [1] of [2] | 真实音色：[1] 的 [2] | 原曲音色：[1] / [2] | A | 已落地术语规定 Authentic Tone 译为“原曲音色”，且“[1] of [2]”在计数语境下应译为“[1] / [2]”而非“[1] 的 [2]”。 |
| 21518 | The Gibson Log | Gibson Log | Gibson 日志 | A | The Gibson Log 中 Log 指日志/记录，需翻译，Gibson 保留英文 |
| 22055 | Event Reward: [1] | 事件奖励：[1] | 活动奖励：[1] | A | 根据已落地术语规则，event(活动)应译为活动，原译“事件”错误 |
| 22495 | Hi-mid | 中高 | 中高频 | A | 源文 Hi-mid 指 High-mid（中高频），现译“中高”缺失“频”字，导致术语不完整且与 22494 的“中低频”格式不一致 |
| 22571 | SLAP{L}MISSED! | 击弦{L}失误！ | 拍弦{L}失误！ | A | 根据已落地术语，Slap 统一译为“拍弦”，原译“击弦”不准确。 |
| 22572 | POP{L}MISSED! | 弹出{L}失误！ | 勾拍{L}失误！ | A | 根据规则5，Pop 在贝斯/吉他技法中应译为“勾拍”，而非“弹出” |
| 22762 | Also part of{L}[1] | 也是{L}[1] | 也是{L}[1]的一部分 | A | 原文 'Also part of' 意为“也是……的一部分”，现译漏译了 'part of' 的核心语义，导致句子成分缺失。 |
| 23131 | 6-inline | 6 串联 | 6 联排 | A | 根据已落地术语，inline 统一译为“联排”，原译“串联”不符合既定术语规范。 |
| 23475 | Pentatonic Minor | Pentatonic Minor | 小调五声音阶 | A | Pentatonic Minor 是音乐风格/音阶名称，应译为中文“小调五声音阶”，而非保留英文。 |
| 26735 | Play with the [1] Band. | 与[1]乐队一起弹奏。 | 与[1]乐队一起演奏。 | A | 模型未提供理由，需复核 |
| 26824 | DARK DAYS | DARK DAYS | 黑暗岁月 | A | DARK DAYS 为普通标题，需译为中文，非品牌专名 |
| 26854 | THINGS CHANGE | THINGS CHANGE | 世事变迁 | A | 全大写普通标题需译中文，原译未翻译 |
| 26865 | DEAL WITH THE DEVIL | DEAL WITH THE DEVIL | 与魔鬼交易 | A | 规则18要求全大写普通标题需译为中文，原译保留英文属于漏译。 |
| 26962 | SHORT AND SWEET | SHORT AND SWEET | 短小精悍 | A | 规则18要求全大写普通标题需译为中文，原译未翻译 |
| 26977 | DIVERSITY TRAINING | DIVERSITY TRAINING | 多元化培训 | A | 规则18：全大写普通标题需译中文，DIVERSITY TRAINING 非品牌专名 |
| 27021 | WHAT'S THE PLAN? | WHAT'S THE PLAN? | 计划是什么？ | A | 规则18要求全大写普通标题需译为中文，原译未翻译 |
| 27085 | COMPLEXITY | COMPLEXITY | 复杂度 | A | 已落地术语规定 Complexity 译为“复杂度”，原译未翻译且全大写标题需译中文。 |
| 27109 | Pentatonic Major | Pentatonic Major | 大调五声音阶 | A | 模型未提供理由，需复核 |
| 27211 | Record Crackle | Record Crackle | 唱片噼啪声 | A | Record Crackle 指黑胶唱片的噼啪噪声，属普通描述性术语，应译为中文而非保留英文 |
| 27407 | BLAST FROM THE PAST | BLAST FROM THE PAST | 昔日经典 | A | 规则18要求全大写普通标题需译中文，BLAST FROM THE PAST 在此语境下指代经典老歌，原译未翻译 |
| 27454 | REVIVAL | 复活 | 复兴 | A | 规则18要求全大写普通标题需译为中文，原译保留英文属于漏译。 |
| 27497 | RED CARTRIDGE | RED CARTRIDGE | 红色卡带 | A | 模型未提供理由，需复核 |
| 27781 | Pops look like this: | 勾弦看起来像这样： | 勾拍看起来像这样： | A | 根据规则5，Pop 应统一译为“勾拍”，原译“勾弦”不符合既定术语规范。 |
| 27928 | Time to dive in. | 是时候深入练习了。 | 开始练习吧。 | A | 规则19指出dive into应译为开始练习，原译“深入练习”不符合教学口语习惯 |
| 28379 | Speeding up again... | 正在加速... | 正在加速…… | A | 模型未提供理由，需复核 |
| 28748 | Octave | 八度 | 八度音程 | A | 规则8规定octave在音程任务中保留“八度音程”，原译“八度”不完整。 |
| 28965 | GOLD CARTRIDGE | 金色唱头 | 金色卡带 | A | Rocksmith 中 Cartridge 指游戏卡带/曲目载体，非黑胶唱头 |
| 29027 | BLUES | 布鲁斯 | 蓝调 | A | Rocksmith 风格名 Blues 统一译为“蓝调”，与“融合蓝调”保持一致，避免“布鲁斯”混用 |
| 29077 | SLAPPIN' THE BASS | SLAPPIN' THE BASS | 拍弦贝斯 | A | 规则18要求全大写普通标题译中文，且规则5规定Slap译为拍弦，原译保留英文错误 |
| 29108 | CLIMBING THE CHARTS | CLIMBING THE CHARTS | 登上排行榜 | A | 规则18要求全大写普通标题需译为中文，原译未翻译 |
| 29277 | SELECTIVE STUDIES | SELECTIVE STUDIES | 选择性研究 | A | 规则18要求全大写普通标题译中文，SELECTIVE STUDIES 应译为“选择性研究” |
| 29281 | PUTTING IT TOGETHER | PUTTING IT TOGETHER | 综合运用 | A | 根据规则18，全大写普通标题需译中文，原译未翻译 |
| 29287 | HOLD IT RIGHT THERE | HOLD IT RIGHT THERE | 就停在这里 | A | 根据规则18，全大写普通标题需译为中文，现译保留英文为漏译。 |
| 29303 | TIME TO REARRANGE | TIME TO REARRANGE | 时间到了，重新排列 | A | 全大写普通标题需译为中文，原译未翻译 |
| 29346 | GROOVE | 放克 | 律动 | A | 模型未提供理由，需复核 |
| 30062 | LYDIAN JAM | LYDIAN JAM | 利底亚即兴 | A | 规则18要求全大写普通标题译中文，LYDIAN JAM 为风格/模式名，非品牌专名，应译为利底亚即兴。 |
| 30068 | DORIAN FUNK | DORIAN FUNK | 多利亚放克 | A | Dorian 是音阶名称，应译为“多利亚”，原译保留英文不符合中文本地化规范 |
| 30100 | SIMPLE BLUES | SIMPLE BLUES | 简单布鲁斯 | A | SIMPLE BLUES 是风格名，应译为中文，现译保留英文违反规则18 |
| 30120 | COMPLEX BLUES | COMPLEX BLUES | 复杂布鲁斯 | A | 规则18要求全大写普通标题需译为中文，'COMPLEX BLUES'是风格/难度描述而非品牌专名 |
| 30257 | HEAVY METAL | HEAVY METAL | 重金属 | A | 风格名应译为中文，原译保留英文不符合本地化规范 |
| 30808 | Phase | 相位 | 阶段 | A | 在 Rocksmith 语境中，Phase 通常指歌曲的段落或阶段，而非物理学的相位。 |
| 31532 | SYNTH FILTER | SYNTH FILTER | 合成器滤波 | A | 规则12及18要求效果器名称按功能翻译且全大写标题需译中文，SYNTH FILTER应译为合成器滤波。 |
| 31709 | BODY | BODY | 琴身 | A | 在乐器语境下，BODY 指吉他/贝斯的琴身，原译保留英文不符合中文本地化要求 |
| 31878 | BASS INTERFACE | 贝斯接口 | 贝斯界面 | A | 模型未提供理由，需复核 |
| 31897 | WELL-ROOTED | WELL-ROOTED | 根基深厚 | A | 全大写普通标题需译中文，原译未翻译 |
| 32699 | A Minor | A Minor | A小调 | A | A Minor 指调性，应译为 A小调，而非保留英文 |
| 32700 | E Minor | E Minor | E小调 | A | E Minor 是调性名称，应译为“E小调”而非保留英文 |
| 32703 | F Major | F Major | F大调 | A | F Major 指调性，应译为 F大调，而非保留英文 |
| 32707 | F Minor | F Minor | F 小调 | A | F Minor 指 F 小调，原译保留英文 Minor 未翻译，且音名与调性间应有空格 |
| 33078 | Modulated Chorus | Modulated Chorus | 调制合唱 | A | Chorus 在效果器语境下标准译名为合唱，Modulated 译为调制，原译保留英文未翻译 |
| 33111 | POST-CHORUS | POST-CHORUS | 后置合唱 | A | 模型未提供理由，需复核 |
| 33122 | VERSE | VERSE | 主歌 | A | 模型未提供理由，需复核 |
| 33376 | Double Stop Riffs | Double Stop Riffs | 双音里夫 | A | Double Stop 是吉他演奏术语，指同时弹奏两个音，应译为“双音”；Riffs 译为“里夫”或“连复段”，原译未翻译。 |
| 34188 | slaps | 击弦 | 拍弦 | A | 根据规则5，Slap 应译为拍弦，原译击弦错误 |
| 34189 | pops | 勾弦 | 勾拍 | A | 根据规则5，Pop 应统一译为“勾拍”，现译“勾弦”不准确。 |
| 34272 | Slaps and Pops | Slap 和 Pop | 拍弦和勾拍 | A | 根据规则5，Slap 应译为拍弦，Pop 应译为勾拍，原译保留英文不符合中文本地化要求 |
| 34289 | Modulated Chorus | Modulated Chorus | 调制合唱 | A | 模型未提供理由，需复核 |
| 34388 | slaps | 击弦 | 拍弦 | A | 根据规则5，Slap 应译为拍弦，而非击弦 |
| 34389 | pops | 勾弦 | 勾拍 | A | 规则5及已落地术语规定Pop统一译为“勾拍”，原译“勾弦”不符合规范。 |
| 34473 | Modulated Chorus | Modulated Chorus | 调制合唱 | A | Chorus 是效果器名称，应译为“合唱”或“合唱效果器”，Modulated Chorus 译为“调制合唱”或“调制合唱效果器”。原译未翻译。 |
| 35483 | Pentatonic Major Jam | Pentatonic Major Jam | 大调五声音阶即兴 | A | Pentatonic Major Jam 中 Pentatonic Major 应译为“大调五声音阶”，Jam 译为“即兴”，整体译为“大调五声音阶即兴”。 |
| 35550 | Noise Rock | Noise Rock | 噪音摇滚 | A | 风格名应译为中文，原译保留英文 |
| 35570 | Jazz Fusion | Jazz Fusion | 爵士融合 | A | Jazz Fusion 是风格名，应译为中文“爵士融合”，而非保留英文 |
| 35606 | Post Funk | 放克后摇 | 后放克 | A | Post Funk 是音乐风格，应译为“后放克”，原译“放克后摇”混淆了风格与摇滚子类型 |
| 35632 | Modern Bluegrass | Modern Bluegrass | 现代蓝草 | A | 规则18要求风格名译为中文，原译保留英文属于漏译。 |
| 35654 | Cartridge Noise | Cartridge Noise | 卡带噪声 | A | Cartridge Noise 指磁带/卡带播放时的底噪，应译为中文效果器/音色名，而非保留英文 |
| 35667 | Acoustic Grunge | Acoustic Grunge | 原声垃圾摇滚 | A | 风格名应译为中文，原译保留英文不符合本地化规范 |
| 35681 | Modern Jazz Rock | Modern Jazz Rock | 现代爵士摇滚 | A | 风格名应译为中文，原译保留英文不符合本地化要求 |
| 35719 | Octave | 八度 | 八度音程 | A | 根据规则8，octave 在音程任务中应保留“八度音程” |
| 35802 | Path: | 路径： | 演奏路径： | A | 根据已落地术语，Path 在 Rocksmith 中统一译为演奏路径 |
| 35856 | SPEED | SPEED | 速度 | A | 模型未提供理由，需复核 |
| 36448 | B flat | B 降 | 降B | A | 音名 B flat 在中文音乐术语中标准译法为“降B”，而非“B 降” |
| 36452 | D flat | D 降 | 降D | A | 音名翻译规范中，降号应置于音名之前，'D 降'不符合中文音乐术语习惯。 |
| 36454 | E flat | E flat | 降E | A | 音名 E flat 在中文音乐语境中通常译为“降E”，保留英文不符合本地化规范 |
| 36455 | E sharp | E sharp | 升E | A | 音名应译为中文，E sharp 即升E |
| 36458 | G flat | G 降 | 降 G | A | 音名译法应为“降 G”而非“G 降” |
| 36580 | C♯ STANDARD | C♯ STANDARD | C♯ 标准调 | A | STANDARD 在此语境指标准调音，应译为中文，现译保留英文为漏译。 |
| 36986 | FIND A SONG... | 查找歌曲... | 查找歌曲…… | A | 规则20要求中文省略号使用“……”，原译使用了半角省略号。 |
| 37203 | Change Path | 改变路径 | 改变演奏路径 | A | 根据已落地术语，Path 在 Rocksmith 语境下统一译为“演奏路径”，原译“路径”过于宽泛且不符合游戏术语规范。 |
| 37204 | Select Path | 选择路径 | 选择演奏路径 | A | 规则14规定Path统一译为演奏路径，原译“路径”不准确 |
| 37213 | AUTHENTIC TONES | 真实音色 | 原曲音色 | A | 已落地术语规定 Authentic Tone 统一译为“原曲音色”，现译“真实音色”不符合术语规范。 |
| 37227 | KEEP GOING | KEEP GOING | 继续 | A | 全大写普通标题需译中文，KEEP GOING 在 UI 中意为继续游戏 |
| 37281 | FIND A PACK... | 寻找一个包... | 寻找一个包…… | A | 规则20要求中文省略号使用“……”，原译使用了半角省略号 |
| 37374 | Switching to bass... | 正在切换到贝斯... | 正在切换到贝斯…… | A | 模型未提供理由，需复核 |

### 桶 B（213）

| id | source | original | revised | 分类 | reason |
|---|---|---|---|---|---|
| 8397 | Here's a quick little riff with that quarter step bend. | 这是一个带有四分之一音阶推弦的短乐句。 | 这是一个带有四分之一音推弦的短乐句。 | B | quarter step 在吉他语境下指四分之一音（semitone 的 1/4），而非“音阶”（scale）；“音阶推弦”易误解为音阶练习或特定音阶内的推弦，应译为“四分之一音推弦”以准确表达音高变化幅度。 |
| 8433 | If you bend this note up a whole step with your third finger{C} it's actually the same note as the first finger playing  | 如果你用第三根手指将这个音符向上推半音{C}它实际上与第一根手指在 B 弦上演奏的音符相同。 | 如果你用第三根手指将这个音符向上推全音{C}它实际上与第一根手指在 B 弦上演奏的音符相同。 | B | 原文 'whole step' 指全音，现译误作半音 |
| 8468 | Your fourth finger holds down this note while your third finger bends the other one up. | 你的无名指按住这个音符，同时中指将另一个音符推弦。 | 你的小指按住这个音符，同时无名指将另一个音符向上推弦。 | B | 原文 fourth finger 对应小指，third finger 对应无名指，现译手指名称错误且漏译 up 方向 |
| 8543 | Now let's get going on palm mutes. | 现在让我们开始练习手掌护弦。 | 现在让我们开始练习手掌制音。 | B | 术语统一：palm mute 应译为“手掌制音”，而非“手掌护弦”。 |
| 8558 | Now here's a riff built out of palm mutes. | 现在来看一个由闷音构成的乐句。 | 现在来看一个由手掌制音构成的乐句。 | B | 术语统一：palm mute 应译为“手掌制音”，原译“闷音”不够精确且不符合已落地术语规范。 |
| 8561 | Here's a riff that shifts back and forth between palm mutes and regular notes. Just lift up your hand when the regular n | 这是一个在闷音和普通音符之间切换的乐句。当普通音符出现时，只需抬起手即可。 | 这是一个在手掌制音和普通音符之间切换的乐句。当普通音符出现时，只需抬起手即可。 | B | 原文 palm mutes 对应已落地术语“手掌制音”，现译“闷音”不准确 |
| 9221 | Good{C} now we'll try switching between chords and frethand mutes. Push down the strings to make the chord when you want | 很好{C} 现在我们来试试在和弦与左手闷音之间切换。按住琴弦形成和弦以发出声音，然后松开以闷音。只是不要完全抬起手指离开琴弦。 | 很好{C} 现在我们来试试在和弦与左手制音之间切换。按住琴弦形成和弦以发出声音，然后松开以制音。只是不要完全抬起手指离开琴弦。 | B | 原文 frethand mutes 对应术语“左手制音”，mute 在演奏语境下译为“制音”更准确，避免与音频静音混淆。 |
| 9360 | To slap{C} you kind of whack the string with the side of your thumb knuckle. | 要击弦{C} 你用拇指指关节侧面敲击琴弦。 | 要拍弦{C} 你用拇指指关节侧面敲击琴弦。 | B | 规则5规定Slap统一译为拍弦，原译“击弦”不准确 |
| 9366 | The thumb actually knocks the bass string into the fretboard{C} and that's what gives you that cool slapping sound. | 实际上是大拇指敲击贝斯琴弦使其撞击指板{C}这就是那种酷炫的击弦声的来源。 | 实际上是大拇指敲击贝斯琴弦使其撞击指板{C}这就是那种酷炫的拍弦声的来源。 | B | 原文 slapping sound 对应贝斯拍弦技法，现译误作击弦 |
| 9382 | Popping isn't quite as tricky as slapping{C} but it still takes some practice. | Pop 技巧不像 Slap 那么难{C} 但仍需一些练习。 | 勾拍不像拍弦那么难{C} 但仍需一些练习。 | B | 已落地术语 Slap=拍弦、Pop=勾拍，原译保留英文错误 |
| 9386 | Palm mutes work great whether you're playing single notes{C} double stops{C} or power chords. | 手掌护弦在演奏单音时{C}双音{C}或强力和弦时都很有效。 | 手掌制音在演奏单音时{C}双音{C}或强力和弦时都很有效。 | B | 术语统一：Palm mute 已落地术语为“手掌制音”，原译“手掌护弦”不准确。 |
| 9395 | You'll find these palm mute power chords are all over the place in hard rock and metal. Check out this riff. | 你会发现这些手掌闷音强力和弦在硬摇滚和金属乐中随处可见。看看这个乐句。 | 你会发现这些手掌制音强力和弦在硬摇滚和金属乐中随处可见。看看这个乐句。 | B | 已落地术语 palm mute=手掌制音，原译“手掌闷音”不符合术语规范。 |
| 9399 | Palm mutes aren't just for single notes... they work great with double stops too. Check this out. | 手掌护弦不仅适用于单音，配合双音效果也很棒。试试看。 | 手掌制音不仅适用于单音，配合双音效果也很棒。试试看。 | B | 已落地术语规定 palm mute 译为手掌制音，现译“手掌护弦”错误 |
| 9404 | And here's a riff using that palm mute double stop... this one's a little more melodic. | 这里有一个使用那种手掌闷音双音的乐句……这个稍微更有旋律感。 | 这里有一个使用那种手掌制音双音的乐句……这个稍微更有旋律感。 | B | 术语统一：palm mute 应译为“手掌制音”，而非“手掌闷音”。 |
| 9478 | Your second finger will go right in the middle of the fret{C} but your third finger will need to get wedged in there bet | 你的食指将放在品的正中间{C}但你的中指需要挤在食指和品丝之间。诀窍是确保它不碰到其他琴弦。 | 你的第二指将放在品的正中间{C}但你的第三指需要挤在第二指和品丝之间。诀窍是确保它不碰到其他琴弦。 | B | 规则4：指法编号需使用明确的手指名称，second finger 应译为“第二指”或“中指”，third finger 应译为“第三指”或“无名指”，原译“食指/中指”与原文指代不符 |
| 9573 | Then put your third finger on the 5th fret of the D string - there's that classic power chord shape again. | 然后将你的第三根手指放在D弦的第5品——又是那个经典强力和弦指型。 | 然后将你的无名指放在D弦的第5品——又是那个经典强力和弦指型。 | B | 规则4要求指法编号使用明确的手指名称，第三指对应无名指 |
| 9799 | With those two shapes you can play any major chord you want{C} all up and down the fretboard. Let's try mixing up both s | 使用这两种指型，你可以演奏任何大调三和弦{C}在指板上上下移动。这次让我们尝试混合使用这两种指型。 | 使用这两种指型，你可以演奏任何大三和弦{C}在指板上上下移动。这次让我们尝试混合使用这两种指型。 | B | 根据规则8，major chord 应译为“大三和弦”，原译“大调三和弦”混淆了调性与和弦种类。 |
| 9924 | Your second finger... your third finger... and your pinky | 你的第 2 指……你的第 3 指……还有你的小指 | 你的食指……你的中指……还有你的小指 | B | 规则4要求指法编号使用明确的手指名称，第2指对应食指，第3指对应中指。 |
| 10207 | That way you can strum across all the strings and only hear the two that make up the octave. | 这样你就可以扫过所有琴弦，只听到构成八度的两根弦的声音。 | 这样你就可以扫过所有琴弦，只听到构成八度音程的两根弦的声音。 | B | 规则8要求 octave 在音程任务中保留“八度音程”，原译“八度”指代不明，易与八度音阶混淆。 |
| 10671 | Let's work on giving the notes themselves some character... we can add vibrato{C} palm mutes{C} and other stuff to the n | 让我们努力赋予音符本身一些个性……我们可以添加颤音{C} 闷音{C} 以及其他技巧，在滑音和推弦之间运用，以创造出真正动人的声音。 | 让我们努力赋予音符本身一些个性……我们可以添加颤音{C} 手掌制音{C} 以及其他技巧，在滑音和推弦之间运用，以创造出真正动人的声音。 | B | 根据已落地术语，palm mute 应译为“手掌制音”而非“闷音” |
| 11326 | It's your frethand doing the muting here. Your other hand doesn't do anything different than it normally does. | 这里是用左手进行闷音。你的右手操作与平时无异。 | 这里是用左手进行制音。你的右手操作与平时无异。 | B | 原文 'frethand' 为 'fret hand' 的拼写错误，指按弦手（左手），现译误作闷音动作主体，且 'muting' 在此语境下指制音而非闷音（palm mute），需修正为制音并明确左手操作。 |
| 11335 | Let's do that again{C} but this time you'll only mute every other note. Just play the rest normally. | 让我们再试一次{C} 但这次你只需闷音每隔一个音符。其余音符正常演奏。 | 让我们再试一次{C} 但这次你只需对每隔一个音符进行制音。其余音符正常演奏。 | B | 原译“闷音”不符合已落地术语“palm mute=手掌制音”及规则5中避免混合表达的要求，且“闷音”作为动词在中文语境中不如“制音”准确对应 mute 动作。 |
| 11448 | Alright{C} so you fret the first note with your first finger{C} then hammer-on to this note{C} 2 frets up{C} with your r | 好的{C}所以你用食指按第一个音符{C}然后上滑音到这个音符{C}高两品{C}用无名指。 | 好的{C}所以你用食指按第一个音符{C}然后击弦到这个音符{C}高两品{C}用无名指。 | B | hammer-on 是击弦（Hammer-on），不是上滑音（Slide）。 |
| 11464 | Then hammer-on that next note with your third finger{C} and slide on up two more frets to the third note. | 然后用你的第三根手指做击弦音到下一个音符{C}再向上滑两个品到第三个音符。 | 然后用你的无名指做击弦音到下一个音符{C}再向上滑两个品到第三个音符。 | B | 规则4：third finger 对应无名指，原译“第三根手指”不符合指法编号明确手指名称的要求。 |
| 11564 | Now let's get going on palm mutes. | 现在让我们开始练习手掌护弦。 | 现在让我们开始练习手掌制音。 | B | 已落地术语 palm mute 应译为手掌制音，现译手掌护弦不符 |
| 11577 | Usually you'll get several palm mutes in a row{C} so let's try repeating it a few times. | 通常你会连续进行几次手掌护弦{C}所以让我们试着重复几次。 | 通常你会连续进行几次手掌制音{C}所以让我们试着重复几次。 | B | 已落地术语规定 palm mute 统一译为手掌制音，现译手掌护弦不符。 |
| 11581 | Now here's a riff built out of palm mutes. | 现在来看一个由闷音构成的乐句。 | 现在来看一个由手掌制音构成的乐句。 | B | 已落地术语规定 palm mute=手掌制音，原译“闷音”不符合术语规范。 |
| 11585 | Let's check out another palm mute riff. | 我们来看看另一个手掌闷音乐句。 | 我们来看看另一个手掌制音乐句。 | B | 术语统一：palm mute 应译为“手掌制音”，而非“手掌闷音”。 |
| 11589 | Here's a riff that shifts back and forth between palm mutes and regular notes. Just lift up your hand when the regular n | 这是一个在闷音和普通音符之间切换的乐句。当普通音符出现时，只需抬起手即可。 | 这是一个在手掌制音和普通音符之间切换的乐句。当普通音符出现时，只需抬起手即可。 | B | 根据已落地术语，palm mute 应译为“手掌制音”，原译“闷音”不够准确。 |
| 12204 | ...but if you're playing without a pick{C} you can still palm mute by playing the notes with your thumb. | ... 但如果你不用拨片弹奏{C} 你仍然可以用拇指拨弦来实现手掌护弦。 | ... 但如果你不用拨片弹奏{C} 你仍然可以用拇指拨弦来实现手掌制音。 | B | 术语统一：palm mute 应译为“手掌制音”，而非“手掌护弦” |
| 12534 | Then play the regular 12th fret note{C} not as a harmonic. | 然后演奏普通的第 12 品音符{C}而不是泛音。 | 然后演奏普通的第 12 品音符{C}，而不是泛音。 | B | 原文 'not as a harmonic' 为否定状语，中文习惯在 '而不是' 前加逗号以区分主句与否定补充，原译缺少标点导致语意连接生硬，虽非严重错误但加逗号更符合中文阅读习惯且未改变原意。 |
| 13163 | You want to be on the E string... | 你需要在 E 弦上... | 你需要在 E 弦上…… | B | 根据规则20，中文省略号应使用“……”，原译使用了半角省略号。 |
| 13356 | Most basses have four strings. They match the four thickest strings of the guitar{C} but are an octave lower. | 大多数贝斯有四根琴弦。它们对应吉他最粗的四根琴弦{C}，但低一个八度。 | 大多数贝斯有四根琴弦。它们对应吉他最粗的四根琴弦{C}，但低一个八度音程。 | B | 根据规则8，octave 在音程语境中应保留“八度音程”，现译“八度”不够精确。 |
| 13626 | You can also combine slap and pop with frethand mutes. | 你还可以将击弦和弹弦与左手制音结合使用。 | 你还可以将拍弦和勾拍与左手制音结合使用。 | B | 已落地术语规定 Slap 译为“拍弦”，Pop 译为“勾拍”，现译“击弦和弹弦”错误。 |
| 13630 | Now here's a riff that uses slap and popped frethand mutes. | 接下来是一个使用击弦和闷音技巧的乐句。 | 接下来是一个使用拍弦和左手制音技巧的乐句。 | B | 根据规则5和已落地术语，Slap应译为拍弦，fret-hand mute应译为左手制音，原译“击弦”和“闷音”不准确。 |
| 17304 | That's plenty of volume. Now get quiet by muting the strings with your hand. | 音量足够了。现在用手闷住琴弦，把声音变小。 | 音量足够了。现在用手掌制音，让声音变小。 | B | 原文 muting the strings with your hand 在吉他演奏语境中通常指手掌制音（palm mute），现译“用手闷住琴弦”表述模糊且不符合术语规范，应明确为手掌制音。 |
| 17449 | Play the string and gently turn your tuning peg in the direction indicated. | 演奏琴弦并轻轻按指示方向转动调弦钮。 | 弹奏琴弦并轻轻按指示方向转动调弦钮。 | B | 规则1：Play the string 在调音语境下指拨动琴弦发声，而非演奏乐曲，原译“演奏”对象不准确。 |
| 17884 | Slides | 滑弦 | 滑音 | B | 已落地术语规定 slide=滑音，原译“滑弦”不符合术语规范。 |
| 18250 | Riff Repeater is a comprehensive practice mode for mastering individual sections of a song. You'll be able to choose whi | 乐句重复器是一种全面的练习模式，用于掌握歌曲的特定段落。您可以选择想要练习的歌曲段落{C}然后选择练习方式。 | 乐句重复器是一种全面的练习模式，用于掌握歌曲的特定段落。你可以选择想要练习的歌曲段落{C}然后选择练习方式。 | B | 根据规则5，玩家应用“你”，原译“您”不符合规范。 |
| 18418 | You are now ready to play an E-major chord. | 你现在可以弹奏 E 大调和弦了。 | 你现在可以弹奏 E 大三和弦了。 | B | 根据规则8，major chord 应译为“大三和弦”，原译“大调和弦”混淆了调性与和弦种类。 |
| 18434 | Now add your third finger to the third fret of the green highlighted string. | 现在将第三根手指按在绿色高亮琴弦的第三品上。 | 现在将中指按在绿色高亮琴弦的第三品上。 | B | 规则4要求指法编号使用明确的手指名称，第三指对应中指 |
| 18439 | You are ready to play the D-major chord. | 你可以演奏 D 大调和弦了。 | 你可以演奏 D 大三和弦了。 | B | 根据规则8，major chord 应译为“大三和弦”，原译“D 大调和弦”混淆了调性与和弦种类。 |
| 18502 | These are palm mutes. | 这些是闷音。 | 这些是手掌制音。 | B | 已落地术语规定 palm mute 译为手掌制音，现译“闷音”不准确。 |
| 18503 | Palm muting is a technique used to create a more percussive sound. | 手掌闷音是一种用于营造更具打击感音色的技巧。 | 手掌制音是一种用于营造更具打击感音色的技巧。 | B | 已落地术语规定 palm mute 为手掌制音，原译“手掌闷音”不符合规范。 |
| 18505 | Palm muting is a technique performed with your picking hand. | 手掌护弦是一种用拨弦手演奏的技巧。 | 手掌制音是一种用拨弦手演奏的技巧。 | B | 已落地术语规定 palm mute=手掌制音，原译“手掌护弦”错误。 |
| 18511 | Be sure to have your hand against the bridge when you play palm mutes. | 演奏手掌闷音时，确保手掌抵住琴桥。 | 演奏手掌制音时，确保手掌抵住琴桥。 | B | 术语统一：palm mute 应译为手掌制音 |
| 18578 | Once you learn a scale pattern you can move and use it anywhere on the fretboard. | 一旦你学会一个音阶模式，你就可以在指板的任何位置移动并使用它。 | 一旦你学会一个音阶指型，你就可以在指板的任何位置移动并使用它。 | B | 根据规则9，Scale Shape 应统一译为“音阶指型”，现译“音阶模式”不符合术语规范。 |
| 18694 | As you play the game{C} experiment with combinations of down strums{C} up strums -- and muting - to create different str | 随着你游玩游戏{C}尝试组合下扫{C}上扫——以及闷音——来创造不同的扫弦模式。 | 随着你游玩游戏{C}尝试组合下扫{C}上扫——以及制音——来创造不同的扫弦模式。 | B | 术语统一：muting 在吉他语境下通常译为“制音”，与 palm mute 保持一致。 |
| 18821 | Notes landing in the first fret of the highlighted zone are played with the first finger{C} and so on for the second{C}  | 落在高亮区域第一品的音符用第一指演奏{C}第二品{C}第三品和第四品依次类推。 | 落在高亮区域第一品的音符用食指演奏{C}第二品{C}第三品和第四品依次类推。 | B | 规则4要求指法编号使用明确的手指名称，第一指应译为食指 |
| 18870 | Learn{C} practice{C} and master palm mutes. | 学习{C}练习{C}并掌握手掌闷音。 | 学习{C}练习{C}并掌握手掌制音。 | B | 已落地术语 palm mute=手掌制音，现译“闷音”不符规范 |
| 18907 | These are palm mutes. | 这些是闷音。 | 这些是手掌制音。 | B | 已落地术语规定palm mute译为手掌制音，原译闷音不准确 |
| 18923 | Place your third finger on the second fret of the blue highlighted  string. | 将中指放在蓝色高亮琴弦的第二品上。 | 将无名指放在蓝色高亮琴弦的第二品上。 | B | 规则4：第三指对应无名指，原译“中指”错误 |
| 18932 | This is the D-major chord shape. | 这是 D 大调和弦指型。 | 这是 D 大三和弦指型。 | B | 规则8要求 major chord 译为大三和弦，原译“大调”混淆了调性与和弦种类。 |
| 18989 | Extra Techniques:{L}Fret Hand Muting | 额外技巧：{L}按弦手闷音 | 额外技巧：{L}左手制音 | B | 模型未提供理由，需复核 |
| 18995 | Learn muting techniques for advanced chords and double stops. | 学习护弦技巧以演奏高级和弦和双音。 | 学习制音技巧以演奏高级和弦和双音。 | B | 已落地术语规定 fret-hand mute 为左手制音，palm mute 为手掌制音，通用 muting 应译为制音，而非护弦。 |
| 18996 | Learn how to mute strings for advanced chords and double stops. | 学习如何护弦以演奏高级和弦和双音。 | 学习如何制音以演奏高级和弦和双音。 | B | 原文 mute strings 在吉他语境下指制音（muting），而非护弦（通常指护弦片或防止杂音的特定动作，但此处指主动制音技巧）；且“护弦”易产生歧义，标准术语为“制音”。 |
| 18999 | Learn how to play fret hand mutes. | 学习如何演奏按弦护弦。 | 学习如何演奏左手制音。 | B | 术语统一：fret hand mutes 对应“左手制音”，原译“按弦护弦”不准确，fret hand 是左手（按弦手），mute 是制音/闷音。 |
| 19008 | Learn{C} practice{C} and master fret hand muting. | 学习{C}练习{C}并掌握左手闷音技巧。 | 学习{C}练习{C}并掌握左手制音技巧。 | B | 已落地术语规定 fret-hand mute 译为“左手制音”，现译“左手闷音”不符合术语规范。 |
| 19019 | Palm Mute Challenge | 手掌闷音挑战 | 手掌制音挑战 | B | 已落地术语规定 palm mute 应译为“手掌制音”，现译“手掌闷音”不符合术语规范。 |
| 19026 | Fret Hand Muting Challenge | 按弦手制音挑战 | 左手制音挑战 | B | 根据已落地术语，fret-hand mute 应译为“左手制音”，而非“按弦手制音”。 |
| 19028 | Palm Mute Challenge | 手掌闷音挑战 | 手掌制音挑战 | B | 已落地术语规定 palm mute=手掌制音，现译“闷音”不符合术语规范。 |
| 19154 | Palm Mutes Unlocked | 已解锁手掌护弦 | 已解锁手掌制音 | B | 根据已落地术语，palm mute 统一译为“手掌制音”，原译“手掌护弦”不准确 |
| 19326 | Arrangements Included: Chord{C} Combo{L}{L}NOTE: Available arrangements will vary by song. Rocksmith™ game disc is requi | 包含编曲：和弦{C}连击{L}{L}注意：可用编曲因歌曲而异。游玩需Rocksmith™游戏光盘。音乐版权信息请访问www.rocksmith.com。 | 包含编曲：和弦{C}一体式音箱{L}{L}注意：可用编曲因歌曲而异。游玩需Rocksmith™游戏光盘。音乐版权信息请访问www.rocksmith.com。 | B | 术语错误：Combo 在吉他设备语境下译为“一体式音箱”，而非“连击”。 |
| 20044 | Tremolo the other strings{L}to switch lanes! | 颤音拨动其他琴弦{L}以切换赛道！ | 快速反复拨动其他琴弦{L}以切换赛道！ | B | 规则6：tremolo 在演奏动作语境下应译为“快速反复拨弦”，而非“颤音”。 |
| 21316 | Palm Mute Accuracy: | 手掌护弦准确率： | 手掌制音准确率： | B | 已落地术语规定 palm mute=手掌制音，现译“手掌护弦”错误。 |
| 21318 | Harmonic Accuracy: | 和声准确度： | 泛音准确度： | B | Harmonic Accuracy 在 Rocksmith 中特指泛音（Harmonics）的判定准确度，而非和声（Harmony）；规则5指出泛音需强调特定位置轻触，此处术语需对应演奏技法。 |
| 21981 | A slide is performed by playing a note and then sliding your finger along the fretboard to another note. | 滑音是通过演奏一个音符，然后沿指板滑动手指到另一个音符来完成的。 | 滑音是通过弹奏一个音符，然后沿指板滑动手指到另一个音符来完成的。 | B | 规则1：弹奏音符应用“弹奏”而非“演奏” |
| 21995 | New Technique Unlocked: Palm Mutes | 解锁新技术：手掌护弦 | 解锁新技术：手掌制音 | B | 术语统一：Palm Mutes 已落地术语为“手掌制音”，原译“手掌护弦”不准确。 |
| 22245 | Let’s start off by playing on the 3rd fret on the yellow string.  Place your first finger here.  To play a fifth higher{ | 让我们从黄色琴弦的第3品开始演奏。将第一根手指放在这里。要演奏高五度音{C} 将第3或第4根手指放在蓝色琴弦的第5品。 | 让我们从黄色琴弦的第3品开始演奏。将食指放在这里。要演奏高五度音{C} 将无名指或小指放在蓝色琴弦的第5品。 | B | 根据规则4，指法编号需使用明确手指名称，第一指为食指，第三/四指为无名指/小指，原译“第一根手指”等表述不准确。 |
| 22247 | To play an octave{C} place your 3rd or 4th finger on the 5th fret of the orange string.  This shape can also be played a | 要演奏八度音{C}请将第3或第4指按在橙色琴弦的第5品。此指型也可在指板的任意位置演奏。 | 要演奏八度音程{C}请将第3或第4指按在橙色琴弦的第5品。此指型也可在指板的任意位置演奏。 | B | 规则8规定 octave 在音程任务中保留“八度音程”，原译“八度音”不准确。 |
| 22249 | These are slap and pop notes. | 这些是拍击和勾弦音符。 | 这些是拍弦和勾拍音符。 | B | 根据规则5，Slap应译为拍弦，Pop应译为勾拍，原译“拍击”和“勾弦”不符合术语规范。 |
| 22250 | Slap and pop is a technique that adds a percussive flair to bass playing. | 击打和勾弦是一种为贝斯演奏增添打击乐色彩的技法。 | 拍弦和勾拍是一种为贝斯演奏增添打击乐色彩的技法。 | B | 根据已落地术语，Slap 应译为拍弦，Pop 应译为勾拍，原译击打和勾弦不准确。 |
| 22258 | After you practice both slapping and popping{C} you can then combine them in succession.  Be sure to use your wrist for  | 练习完击弦和勾弦后{C}你可以将它们连续组合使用。大部分动作请确保使用手腕。建立老茧和击弦贝斯所需的肌肉记忆可能需要一段时间……请坚持练习并经常休息。 | 练习完拍弦和勾拍后{C}你可以将它们连续组合使用。大部分动作请确保使用手腕。建立老茧和拍弦贝斯所需的肌肉记忆可能需要一段时间……请坚持练习并经常休息。 | B | 已落地术语规定 Slap 译为拍弦，Pop 译为勾拍，现译“击弦”和“勾弦”不符合规范。 |
| 22260 | If you are having trouble producing enough sound with a slap{C} make sure to emphasize your thumb bounce. | 如果你发现用击弦技巧发出的声音不够大{C} 请确保强调拇指的回弹动作。 | 如果你发现用拍弦技巧发出的声音不够大{C} 请确保强调拇指的回弹动作。 | B | Slap 在贝斯技法中应译为“拍弦”，而非“击弦”。 |
| 22381 | Slides | 滑弦 | 滑音 | B | 术语统一：slide 在吉他技法中标准译名为“滑音”，而非“滑弦”。 |
| 22429 | For slaps{C} bounce your thumb off the string immediately after striking it | 对于击弦{C}在拇指敲击琴弦后立即弹起 | 对于拍弦{C}在拇指敲击琴弦后立即弹起 | B | 术语统一：Slap 在贝斯/吉他技法中标准译名为“拍弦”，而非“击弦”。 |
| 22430 | For pops{C} rotate your wrist after you pluck to mute the string with the side of your hand | 对于拨弦{C}拨弦后转动手腕，用手侧压住琴弦以制音 | 对于勾拍{C}拨弦后转动手腕，用手侧压住琴弦以制音 | B | 原文 'For pops' 指贝斯勾拍技法，根据规则5应译为“勾拍”而非“拨弦” |
| 22442 | An advanced technique used in multiple bass styles{C} slap and pop adds a percussive flair to your bass playing. | 一种用于多种贝斯风格的进阶技巧{C} 拍击与拨片弹出为你的贝斯演奏增添打击乐般的色彩。 | 一种用于多种贝斯风格的进阶技巧{C} 拍弦与勾拍为你的贝斯演奏增添打击乐般的色彩。 | B | 根据规则5，Slap应译为拍弦，Pop应译为勾拍，原译“拨片弹出”错误且混淆了动作对象。 |
| 22449 | New Technique Unlocked: Octaves & Fifths | 解锁新技术：八度与五度 | 解锁新技术：八度音程与五度音程 | B | 根据规则8，octave 在音程任务中应保留“八度音程”，fifths 同理应为“五度音程”，原译“八度与五度”不够准确。 |
| 22450 | New Technique Unlocked: Slap & Pop | 解锁新技术：击勾弦 | 解锁新技术：拍弦与勾拍 | B | 根据已落地术语规则，Slap 应译为“拍弦”，Pop 应译为“勾拍”，原译“击勾弦”混淆了术语且不符合规范。 |
| 22658 | To slap{C} use the side of your thumb's knuckle and bounce your string immediately after striking it. | 要演奏击弦{C} 用拇指指关节侧面敲击琴弦，并在敲击后立即弹起。 | 要演奏拍弦{C} 用拇指指关节侧面敲击琴弦，并在敲击后立即弹起。 | B | 根据规则5，贝斯 Slap 应译为“拍弦”，原译“击弦”易与 Hammer-on（击弦）混淆。 |
| 22674 | Learn{C} practice{C} and master octaves & fifths. | 学习{C}练习{C}并掌握八度音与五度音。 | 学习{C}练习{C}并掌握八度音程与五度音程。 | B | octaves & fifths 在乐理教学中指音程，现译误作音高 |
| 22675 | Learn{C} practice{C} and master slap & pop. | 学习{C}练习{C}并掌握击勾弦技巧。 | 学习{C}练习{C}并掌握拍弦与勾拍技巧。 | B | 根据规则5，Slap 应译为拍弦，Pop 应译为勾拍，原译“击勾弦”混淆了术语且不符合规范。 |
| 23473 | Phrygian Dominant | 弗里吉亚属调式 | 弗里吉亚属音阶 | B | 已落地术语规定 Phrygian Dominant 译为“弗里吉亚属音阶”，现译“弗里吉亚属调式”不符合术语规范。 |
| 23483 | These arpeggios are a great opportunity to put down your pick and play the guitar strings with your fingers. | 这些分解和弦是放下拨片、用手指弹奏琴弦的好机会。 | 这些琶音是放下拨片、用手指弹奏琴弦的好机会。 | B | 规则9规定Arpeggio统一译为'琶音'，现译'分解和弦'不符合已落地术语。 |
| 23490 | Let's try playing that arpeggio pattern again{C} but this time{C} try playing it with your fingers. | 让我们再弹一次那个分解和弦模式{C} 但这次{C} 试着用手指弹奏。 | 让我们再弹一次那个琶音模式{C} 但这次{C} 试着用手指弹奏。 | B | 规则9要求 Arpeggio 统一译为“琶音”，原译“分解和弦”虽语义相近但术语不统一，且规则9明确标题与正文应互相对应。 |
| 23759 | Don't forget to put that first finger down on the first fret of the G string. | 别忘了把第一根手指按在 G 弦的第一品上。 | 别忘了把食指按在 G 弦的第一品上。 | B | 规则4要求指法编号使用明确的手指名称，'第一根手指'应译为'食指'。 |
| 23788 | Start with your 1st finger on the 3rd fret of the A string and your 3rd finger on the 5th fret of the D string. | 用第一指按A弦的第3品，第三指按D弦的第5品开始。 | 用食指按A弦的第3品，无名指按D弦的第5品开始。 | B | 规则4要求指法编号使用明确的手指名称，1st finger应为食指，3rd finger应为无名指，原译“第一指”“第三指”不符合规范。 |
| 23820 | Your 2nd finger is on the wrong fret. | 你的食指按错了品。 | 你的中指按错了品。 | B | 原文 '2nd finger' 指第二指（中指），现译误译为食指（第一指） |
| 23825 | Double check that your first finger is still on the 1st fret of the B string and your 2nd finger is on the 2nd fret of t | 请再次确认你的食指仍在B弦第1品，无名指在D弦第2品。这些音符没有响。 | 请再次确认你的食指仍在B弦第1品，中指在D弦第2品。这些音符没有响。 | B | 指法错误：2nd finger 对应中指，原译误译为无名指。 |
| 23833 | There's something going on with the A string. Make sure your 3rd finger is on the 6th fret. | A弦有些问题。请确保你的第3指按在第6品。 | A弦有些问题。请确保你的无名指按在第6品。 | B | 原文 3rd finger 对应中指，现译“第3指”未使用明确手指名称，违反规则4 |
| 23910 | Start with your 1st finger playing the 7th fret of both the B and high E strings. | 用第一指弹奏B弦和高音E弦的第7品开始。 | 用食指弹奏B弦和高音E弦的第7品开始。 | B | 规则4要求指法编号使用明确的手指名称，'1st finger'应译为'食指'而非'第一指'。 |
| 23928 | Your D string is ringing out. Mute it with the underside of your 1st finger so it doesn't sound. | 你的 D 弦在响。请用食指侧面将其闷住，以免发出声音。 | 你的 D 弦在响。请用食指侧面将其制音，以免发出声音。 | B | 术语统一：fret-hand mute 对应“制音”或“闷音”，原译“闷住”口语化且未体现技术动作，且“以免发出声音”略显冗余，但主要问题是动词选择，建议用更准确的“制音”或保留“闷住”但需确认语境，此处“制音”更符合 Rocksmith 教学术语习惯，不过原译“闷住”在口语教学中也可接受，但“以免 |
| 23930 | Start with your 1st finger on the 2nd fret of the A string and your 3rd finger on the 4th fret of the G string. Be sure  | 食指按在 A 弦第 2 品，中指按在 G 弦第 4 品。扫弦时务必制音其他琴弦，只让这两根弦发声。 | 食指按在 A 弦第 2 品，无名指按在 G 弦第 4 品。扫弦时务必制音其他琴弦，只让这两根弦发声。 | B | 原文 3rd finger 对应无名指，现译误作中指 |
| 24140 | Then{C} look down at your guitar and count the same number of strings down from your own top string. | 然后{C}低头看你的吉他，从你自己的最细弦开始数相同数量的弦。 | 然后{C}低头看你的吉他，从你自己的最细弦开始向下数相同数量的弦。 | B | 原文 'count ... down from' 明确指示了计数的方向是向下（从细弦向粗弦），原译漏译了方向词 'down'，导致指令不完整。 |
| 24181 | Play the double stop on the 7th fret{C} and then pull-off to the 5th fret. | 在第7品弹奏双音{C}然后拨弦至第5品。 | 在第7品弹奏双音{C}，然后拨弦至第5品。 | B | 原文 'and then' 连接两个动作，中文习惯在并列动作间加逗号以符合排版规范（规则20），且 'pull-off' 译为 '拨弦' 符合吉他教学语境（规则1/5）。 |
| 24259 | Something's a little off here... Your picking hand might be too far from bridge. Slide it back a little more and try the | 这里有点不对劲……你的拨弦手可能离琴桥太远了。稍微往回移一点，再试试手掌护弦。 | 这里有点不对劲……你的拨弦手可能离琴桥太远了。稍微往回移一点，再试试手掌制音。 | B | 术语统一：palm mute 应译为“手掌制音”，而非“手掌护弦”。 |
| 24338 | You're not sliding quite far enough. This goes all the way up to the 5th fret. | 你的滑弦距离还不够。这个滑弦要一直滑到第5品。 | 你的滑音距离还不够。这个滑音要一直滑到第5品。 | B | 术语统一：slide 应译为“滑音”而非“滑弦” |
| 24549 | Start with your 1st finger on the 5th fret of the E string and your 3rd or 4th finger on the 7th fret of the A string. | 食指按在 E 弦第 5 品，中指或无名指按在 A 弦第 7 品。 | 食指按在 E 弦第 5 品，无名指或小指按在 A 弦第 7 品。 | B | 原文 3rd or 4th finger 对应中指或无名指，现译错误，需修正为无名指或小指。 |
| 24652 | The note got muted after you played it. Make sure your thumb bounces off the string after you slap it{C} so the note can | 音符在弹奏后被制音了。确保拇指在拍击琴弦后弹开{C} 以便音符能够延音。 | 音符在弹奏后被制音了。确保拇指在拍弦后弹开{C} 以便音符能够延音。 | B | 原文 slap 对应贝斯拍弦技法，现译“拍击琴弦”不够准确，应统一为“拍弦” |
| 24656 | Sounds like you're on the wrong string. This pop happens on the D string. | 听起来弦不对。这个拨弦在D弦上。 | 听起来弦不对。这个勾拍在D弦上。 | B | 规则5要求 Pop 译为“勾拍”，原译“拨弦”混淆了贝斯技法与普通拨弦，且 Pop 特指勾拍动作。 |
| 24657 | Sounds like you're on the A string. This pop happens on the D string. | 听起来你在 A 弦上。这个拨弦在 D 弦上。 | 听起来你在 A 弦上。这个勾拍在 D 弦上。 | B | 术语统一：Pop 应译为“勾拍”，原译“拨弦”混淆了 Slap/Pop 与普通拨弦的区别。 |
| 24661 | Mute the E string with your fretting hand and then slap it with your thumb. | 用按弦手闷住E弦，然后用拇指拨弦。 | 用按弦手闷住E弦，然后用拇指拍弦。 | B | 规则5规定Slap译为拍弦，原译拨弦不准确 |
| 24666 | Sounds like you're starting on the wrong note. This slide starts at the 5th fret. | 听起来起始音符不对。这个滑弦从第 5 品开始。 | 听起来起始音符不对。这个滑音从第 5 品开始。 | B | 术语统一：slide 应译为“滑音”，原译“滑弦”不符合已落地术语规范。 |
| 24843 | Let's try that slap first. | 让我们先试试击弦。 | 让我们先试试拍弦。 | B | 规则5及已落地术语规定贝斯 Slap 统一译为拍弦，原译“击弦”不符合规范。 |
| 24850 | Mute the D string with your fretting hand and then pop it. | 用按弦手闷住 D 弦，然后拨弦。 | 用按弦手闷住 D 弦，然后勾拍。 | B | 原文 pop 在贝斯/吉他语境下特指 Pop 技法，对应中文术语“勾拍”，而非普通拨弦。 |
| 24855 | Mute the strings with your fretting hand{C} then play a muted slap and pop. | 用按弦手闷音{C} 然后演奏闷音的 slap 和 pop。 | 用按弦手制音{C} 然后演奏闷音的拍弦和勾拍。 | B | 术语统一：Mute 译为“制音”；Slap 和 Pop 分别对应已落地术语“拍弦”和“勾拍”，原译保留英文不符合规范。 |
| 24857 | You're getting some extra notes in there. This time{C} try to make your slap and pop clean{C} so you don't get any extra | 你加入了一些额外的音符。这次{C}试着让你的击弦和勾弦干净利落{C}这样就不会发出额外的音符。 | 你加入了一些额外的音符。这次{C}试着让你的拍弦和勾拍干净利落{C}这样就不会发出额外的音符。 | B | 根据已落地术语，Slap 应译为拍弦，Pop 应译为勾拍，原译击弦和勾弦不准确。 |
| 24858 | Sounds like you're getting an open string in there. Make sure you're muting the strings so they can't vibrate when you s | 听起来混进了空弦音。确保闷住琴弦，这样在击弦和勾弦时它们才不会振动。 | 听起来混进了空弦音。确保闷住琴弦，这样在拍弦和勾拍时它们才不会振动。 | B | 根据规则5，Slap应译为拍弦，Pop应译为勾拍，原译“击弦和勾弦”不符合术语规范。 |
| 24932 | Experiment with combining hammer-ons{C} pull-offs{C} slides{C} and mutes with your slap and pop playing. | 尝试将击弦{C} 勾弦{C} 滑音{C} 和闷音与你的拍弦和弹拨演奏结合起来。 | 尝试将击弦{C} 勾弦{C} 滑音{C} 和闷音与你的拍弦和勾拍演奏结合起来。 | B | 术语统一：Pop 在贝斯语境下应译为勾拍 |
| 24982 | Frethand mutes go great with barre chords... you just release the pressure on the strings slightly to get the muted clic | 左手闷音非常适合横按和弦……你只需稍微放松对琴弦的压力以发出闷音咔哒声{C}然后再次按下以发出和弦声。 | 左手制音非常适合横按和弦……你只需稍微放松对琴弦的压力以发出闷音咔哒声{C}然后再次按下以发出和弦声。 | B | 术语统一：已落地术语规定 fret-hand mute 译为“左手制音”，原译“左手闷音”不符合规范。 |
| 24991 | Combining multiple techniques together{C} like palm mutes with pull-offs{C} is a good way to expand the kinds of sounds  | 组合多种技巧{C}例如将手掌护弦与勾弦结合{C}是扩展你使用的音色种类的好方法。 | 组合多种技巧{C}例如将手掌制音与勾弦结合{C}是扩展你使用的音色种类的好方法。 | B | 已落地术语 palm mute 应译为手掌制音，现译手掌护弦不符 |
| 25026 | Take some time to play around with different Roots and get comfortable with the idea of moving the Scale Shape around th | 花点时间尝试不同的根音，并熟悉在指板上移动音阶形状的概念。 | 花点时间尝试不同的根音，并熟悉在指板上移动音阶指型的概念。 | B | 根据规则9和已落地术语，Scale Shape应统一译为“音阶指型”，原译“音阶形状”不准确。 |
| 25027 | Great. Now that you're comfortable with the idea of moving around the Scale Shape{C} let's take a look at a new scale. | 很好。既然你已经习惯了在音阶形状中移动{C}让我们来看看一个新的音阶。 | 很好。既然你已经习惯了在音阶指型中移动{C}让我们来看看一个新的音阶。 | B | 已落地术语 Scale Shape 应译为音阶指型，现译音阶形状不符 |
| 25074 | The Downbeat is the most important beat in a Session because of the impact it has on Harmonicity and Phrasing. Remember{ | 在即兴演奏中，强拍是最重要的节拍，因为它对和谐度与乐句感影响巨大。记住{C}在律动计上{C}强拍的光效比其他节拍更亮。{L}{L}在强拍上弹奏和弦音听起来比平时更和谐。所以，在强拍上弹奏非音阶音会感觉更不和谐{C}对吧？你可以利用这一点来优 | 在即兴演奏中，正拍是最重要的节拍，因为它对和谐度与乐句感影响巨大。记住{C}在律动计上{C}正拍的光效比其他节拍更亮。{L}{L}在正拍上弹奏和弦音听起来比平时更和谐。所以，在正拍上弹奏非音阶音会感觉更不和谐{C}对吧？你可以利用这一点来优 | B | 规则7指出downbeat应译为正拍，原译强拍不符合术语规范 |
| 25150 | Phrygian Dominant is only one note different from Phrygian. Phrygian Dominant has that iconic Spanish guitar sound. Even | 弗里吉亚属调与弗里吉亚调仅有一个音符不同。弗里吉亚属调具有标志性的西班牙吉他音色。尽管它源于古典音乐{C} 但它却是冲浪摇滚和金属乐手公认的最爱。 | 弗里吉亚属音阶与弗里吉亚音阶仅有一个音符不同。弗里吉亚属音阶具有标志性的西班牙吉他音色。尽管它源于古典音乐{C} 但它却是冲浪摇滚和金属乐手公认的最爱。 | B | 已落地术语规定 Phrygian Dominant 译为“弗里吉亚属音阶”，原译“属调”混淆了音阶与调性概念 |
| 25165 | Remember{C} calibration is super important in Session Mode. If you switch guitars{C} or if you feel like the band isn't  | 记住{C}在 Session Mode 中校准非常重要。如果您更换吉他{C}或者感觉乐队没有跟随您的提示{C}请花一点时间重新校准您的吉他。 | 记住{C}在 Session Mode 中校准非常重要。如果你更换吉他{C}或者感觉乐队没有跟随你的提示{C}请花一点时间重新校准你的吉他。 | B | 根据规则5，玩家应使用“你”而非“您”；根据规则13，Session Mode 语境下 session 译为即兴演奏模式或保留英文均可，但此处保留英文符合品牌专名保留原则，且原译中“您”为错误代词。 |
| 25168 | Did you notice that some of the riffs in Learn-A-Song use the same Scale Shapes you came across in Session Mode? It can  | 你注意到“学习歌曲”中的一些乐句使用了你在“即兴演奏”中遇到的相同音阶形状吗？在“即兴演奏”中演奏这些乐句会很有趣。 | 你注意到“学习歌曲”中的一些乐句使用了你在“即兴演奏”中遇到的相同音阶指型吗？在“即兴演奏”中演奏这些乐句会很有趣。 | B | Scale Shape 已落地术语为“音阶指型”，原译“音阶形状”不符合术语规范。 |
| 25373 | Frethand mutes are a great way to add a percussive element to your playing. You just touch the string with your fingers  | 按弦手制音是向演奏中添加打击乐元素的好方法。你只需在弹奏时用手指触碰琴弦以阻止其振动。 | 左手制音是向演奏中添加打击乐元素的好方法。你只需在弹奏时用手指触碰琴弦以阻止其振动。 | B | 术语错误，已落地术语规定 fret-hand mute 应译为“左手制音”，而非“按弦手制音”。 |
| 25435 | You just can't get that classic funky bass sound going without learning how to slap. So stick out your thumb{C} and give | 如果不学会击弦，你就无法获得那种经典的放克贝斯音色。所以伸出你的拇指{C} 用力敲击琴弦。 | 如果不学会拍弦，你就无法获得那种经典的放克贝斯音色。所以伸出你的拇指{C} 用力敲击琴弦。 | B | 规则5规定贝斯 Slap 应译为“拍弦”，原译“击弦”混淆了贝斯技法与普通拨弦/敲击动作 |
| 25443 | Slapping and popping go hand in hand. To pop the string{C} you curl your finger under it{C} pull up{C} and then release. | 击打和勾弦相辅相成。要勾弦{C} 将手指卷到琴弦下方{C} 向上拉{C} 然后松开。 | 拍弦和勾拍相辅相成。要勾拍{C} 将手指卷到琴弦下方{C} 向上拉{C} 然后松开。 | B | 根据规则5，Slap 应译为“拍弦”，Pop 应译为“勾拍”，原译“击打”和“勾弦”不准确。 |
| 25455 | Notes with a big X on them are palm mutes. When you see one of those{C} mute the strings with the heel of your playing h | 带有大 X 标记的音符是手掌护弦。当您看到这种音符时{C} 在演奏音符前，用演奏手的掌根护住琴弦。 | 带有大 X 标记的音符是手掌制音。当您看到这种音符时{C} 在演奏音符前，用演奏手的掌根制音琴弦。 | B | 根据已落地术语，palm mute 应译为“手掌制音”，原译“手掌护弦”不符合术语规范。 |
| 25469 | Combining multiple techniques together{C} like palm mutes with hammer-ons{C} is a great way to expand the variety of sou | 将多种技巧组合在一起{C}例如将手掌护弦与击弦结合{C}是扩展可演奏音色多样性的绝佳方式。 | 将多种技巧组合在一起{C}例如将手掌制音与击弦结合{C}是扩展可演奏音色多样性的绝佳方式。 | B | 已落地术语规定 palm mute=手掌制音，原译“手掌护弦”错误。 |
| 25474 | Practice your slap bass slowly at first{C} then work on building up your speed. | 起初请慢速练习你的Slap Bass{C}然后努力提升速度。 | 起初请慢速练习拍弦{C}然后努力提升速度。 | B | 原文 slap bass 指拍弦贝斯技法，Slap 对应术语“拍弦”，不应保留英文或译为 Slap Bass。 |
| 25486 | You can combine all kinds of techniques... Let's try a pop with a harmonic. | 你可以组合各种技巧……让我们试试带泛音的击弦。 | 你可以组合各种技巧……让我们试试带泛音的勾拍。 | B | Pop 已落地术语为“勾拍”，原译“击弦”混淆了 Hammer-on 与 Pop 的动作区别。 |
| 25513 | It might take some practice to play the accents while your hand is in a palm mute position{C} but keep at it and you'll  | 在手部处于手掌闷音位置时演奏重音可能需要一些练习{C}但坚持下来，你很快就能掌握。 | 在手部处于手掌制音位置时演奏重音可能需要一些练习{C}但坚持下来，你很快就能掌握。 | B | 已落地术语 palm mute 应译为“手掌制音”，原译“手掌闷音”不符合术语规范。 |
| 25639 | Learning scales is the best way to start mastering riffs and open the door to improvisation. | 学习音阶是掌握乐句并开启即兴演奏的最佳方式。 | 学习音阶是开始掌握乐句并开启即兴演奏之门的最佳方式。 | B | 原文 'start mastering' 对应“开始掌握”，现译漏译了 'start'，导致语义从“开始掌握”变为直接“掌握”，改变了动作的阶段性和程度。 |
| 25650 | Master scales by fighting crime!  Play the highlighted notes to attack{C} and run through the scales to rack up combos. | 大师通过打击犯罪来练习音阶！ 弹奏高亮音符进行攻击{C}并快速通过音阶以累积连击。 | 通过打击犯罪来练习音阶！弹奏高亮音符进行攻击{C}并快速通过音阶以累积连击。 | B | 原文“Master scales by fighting crime”是游戏内的幽默/任务描述，主语隐含为玩家或游戏机制，现译“大师通过...”误将 Master 译为名词“大师”，且语意不通，应译为动作“通过...来练习/掌握”。 |
| 25711 | Scale Warriors is a great way to master multiple Scale Shapes{C} which you can turn right around and apply in Session Mo | 音阶战士是掌握多种音阶型式的绝佳方式{C} 您可以立即在即兴演奏模式中应用。 | 音阶战士是掌握多种音阶指型的绝佳方式{C} 您可以立即在即兴演奏模式中应用。 | B | 已落地术语规定 Scale Shape 统一译为音阶指型，原译“音阶型式”不符合术语规范。 |
| 26068 | Picking hand techniques include things like tremolo{C} palm mutes{C} and accents. | 拨弦手技巧包括颤音{C} 手掌闷音{C} 和重音。 | 拨弦手技巧包括颤音{C} 手掌制音{C} 和重音。 | B | 根据已落地术语，palm mute 应译为“手掌制音”，现译“手掌闷音”不符合规范。 |
| 26588 | Fingerstyle guitar is just what it sounds like – you play the strings with your fingers instead of a pick. You can play  | 指弹吉他顾名思义——用指尖拨弦而非拨片。你可以一次弹奏一个音符{C}或用拇指和手指演奏分解和弦音型。 | 指弹吉他顾名思义——用指尖拨弦而非拨片。你可以一次弹奏一个音符{C}或用拇指和手指演奏琶音。 | B | 术语统一：Arpeggio 应译为“琶音”，而非“分解和弦音型”。 |
| 26672 | Load a Scale Shape: Pentatonic Minor. | 加载音阶形状：小调五声音阶。 | 加载音阶指型：小调五声音阶。 | B | 根据已落地术语，Scale Shape 统一译为音阶指型，现译音阶形状不准确 |
| 26699 | Learn a Scale Shape: Pentatonic Major. | 学习音阶形态：五声音阶大调。 | 学习音阶指型：五声音阶大调。 | B | 术语 Scale Shape 应统一译为“音阶指型”，而非“音阶形态”。 |
| 26754 | Play Chord Tones on the Downbeat | 在重拍上弹奏和弦音 | 在正拍上弹奏和弦音 | B | 根据规则7，downbeat 在拨弦教学中对应正拍，不宜机械译成强拍或重拍。 |
| 26759 | Play Chord Tones on Downbeats to use timing in your Phrasing. | 在强拍上演奏和弦音，利用节奏感进行乐句处理。 | 在正拍上演奏和弦音，利用节奏感进行乐句处理。 | B | 规则7指出downbeat对应正拍，不宜机械译成强拍 |
| 26764 | Use Chord Tones on the Downbeat to ground your Phrasing. | 在重拍上使用和弦音来稳固你的乐句演奏。 | 在正拍上使用和弦音来稳固你的乐句演奏。 | B | 规则7指出 downbeat 对应正拍，不宜机械译成强拍/重拍，现译“重拍”不符合术语规范。 |
| 26828 | Slide the Scale Shape up an Octave. | 将音阶形状上移一个八度。 | 将音阶指型上移一个八度。 | B | Scale Shape 已落地术语为“音阶指型”，原译“音阶形状”不符合术语规范。 |
| 26843 | Learn a Scale Shape: Lydian. | 学习音阶形态：Lydian。 | 学习音阶指型：Lydian。 | B | 根据规则9，Scale Shape 统一译为“音阶指型”，原译“音阶形态”不符合已落地术语。 |
| 26864 | Learn a Scale Shape: Blues. | 学习音阶形态：布鲁斯。 | 学习音阶指型：布鲁斯。 | B | 根据规则9，Scale Shape 统一译为“音阶指型”，原译“音阶形态”不符合已落地术语。 |
| 26872 | Play the Phrygian Dominant Scale Notes. | 演奏弗里吉亚属调音阶音符。 | 演奏弗里吉亚属音阶音符。 | B | 根据已落地术语，Phrygian Dominant 应译为“弗里吉亚属音阶”，而非“弗里吉亚属调音阶”。 |
| 26890 | Play Scale Shapes in a variety of positions along the neck. | 在琴颈的不同位置弹奏多种音阶形态。 | 在琴颈的不同位置弹奏多种音阶指型。 | B | 已落地术语规定 Scale Shape 统一译为音阶指型，原译“音阶形态”不符合术语规范。 |
| 26903 | Explore Session Mode! | 探索即兴演奏！ | 探索即兴演奏模式！ | B | 根据语境例外，Session Mode 应译为“即兴演奏模式”，原译漏译“模式”。 |
| 27001 | HARMONIC? AHHH... | 和声？啊…… | 泛音？啊…… | B | 原文 HARMONIC 在吉他语境下指泛音，现译“和声”错误 |
| 27077 | RETURN TO SESSION MODE | 返回即兴演奏 | 返回即兴演奏模式 | B | 模型未提供理由，需复核 |
| 27106 | Phrygian Dominant | 弗里吉亚属调式 | 弗里吉亚属音阶 | B | 根据已落地术语，Phrygian Dominant 应译为“弗里吉亚属音阶”而非“弗里吉亚属调式” |
| 27151 | Slap Bass | 击打贝斯 | 拍弦贝斯 | B | 根据规则5，Slap 应译为“拍弦”，原译“击打”不准确。 |
| 27773 | Palm mutes look like this: | 手掌闷音看起来像这样： | 手掌制音看起来像这样： | B | 已落地术语：palm mute 统一译为手掌制音，原译“手掌闷音”不符合术语规范。 |
| 27796 | This is a slap frethand mute. | 这是击弦制音。 | 这是拍弦制音。 | B | 原文 'slap' 在贝斯/吉他技法中对应术语 '拍弦'，而非 '击弦'（hammer-on） |
| 27797 | Mute with your frethand while slapping. | 弹击时用左手制音。 | 拍弦时用左手制音。 | B | 原文 slapping 对应贝斯拍弦技法，现译“弹击”不符合已落地术语 Slap=拍弦 |
| 27853 | You want to be on the E string... | 你需要在 E 弦上... | 你需要在 E 弦上…… | B | 中文省略号应使用“……”而非半角“...” |
| 28489 | This is a pop frethand mute: | 这是一个流行风格的制音技巧： | 这是一个流行风格的左手制音技巧： | B | 原文 'frethand mute' 为 'fret-hand mute' 的拼写错误，根据已落地术语规则，fret-hand mute 应译为“左手制音”，现译漏译了“左手”这一关键限定词。 |
| 28707 | Repeat the chord or double stop you just played. | 重复您刚才演奏的和弦或双音。 | 重复你刚才演奏的和弦或双音。 | B | 规则5及代词规则要求玩家用“你”，原译“您”不符合规范。 |
| 28718 | Mute unused strings with your finger. | 用手指闷住未使用的琴弦。 | 用手指制音未使用的琴弦。 | B | 术语统一：Mute 在吉他演奏语境中应译为“制音”或“闷音”，而非“闷住”（后者偏向物理遮挡动作，且不符合已落地术语规范）。 |
| 28981 | POP PERCUSSION | 流行打击乐 | 勾拍打击乐 | B | 根据规则5，Pop 在贝斯/吉他技法中应译为‘勾拍’，而非‘流行’（Pop music）或‘爆音’。此处 'POP PERCUSSION' 指使用 Pop 技法产生的打击乐效果。 |
| 29072 | Raise your Chord Shapes rating. | 提升你的和弦指法评级。 | 提升你的和弦指型评级。 | B | 术语统一：Scale Shape/Chord Shape 对应“指型”，而非“指法” |
| 29232 | PRACTICE MAKES PERFECT | PRACTICE MAKES PERFECT | 熟能生巧 | B | PRACTICE MAKES PERFECT 是常见谚语，应译为中文“熟能生巧”，而非保留英文 |
| 32222 | Slice a ghost at the beginning of a slide. | 在滑动开始时切幽灵。 | 在滑音开始时切一个幽灵音。 | B | Ghost 在演奏语境下指幽灵音，Slice 指切音/制音动作 |
| 32225 | Slice a color-change ghost at the beginning of a slide. | 在滑动开始时切变色幽灵。 | 在滑音开始时切分变色幽灵音符。 | B | 术语准确：ghost 在 Rocksmith 中特指“幽灵音符”（ghosted notes），slide 译为“滑音”更符合吉他教学语境。 |
| 32314 | Change direction [1] times midway through a scale. | 改变方向 [1] 次，在音阶演奏中途。 | 在音阶演奏中途改变方向 [1] 次。 | B | 模型未提供理由，需复核 |
| 32577 | Take off-ramps to shift position on the fretboard and learn new anchors and shapes for the scale. | 驶入出口匝道以在指板上变换位置，并学习音阶的新锚点和指型。 | 使用滑音来在指板上变换位置，并学习音阶的新锚点和指型。 | B | 原文 'Take off-ramps' 是比喻用法，指利用滑音（slide）作为过渡手段来改变把位，而非字面的‘驶入出口匝道’；结合语境 'shift position' 和 'scale'，此处应译为演奏技法‘滑音’。 |
| 32698 | Phrygian Dominant | 弗里吉亚属调式 | 弗里吉亚属音阶 | B | 模型未提供理由，需复核 |
| 33378 | Frethand Mute Basics | 按弦手制音基础 | 左手制音基础 | B | 已落地术语规定 fret-hand mute 译为“左手制音”，现译“按弦手制音”不符合术语规范。 |
| 33379 | Frethand Mute Riffs | 左手闷音乐句 | 左手制音乐句 | B | 术语统一：fret-hand mute 应译为“左手制音”，而非“左手闷音” |
| 33393 | Palm Mutes 101B | 手掌护弦入门 101B | 手掌制音入门 101B | B | 根据已落地术语，palm mute 应译为“手掌制音”，原译“手掌护弦”不符合术语规范。 |
| 33394 | Palm Mute Basics | 手掌护弦基础 | 手掌制音基础 | B | 根据已落地术语，palm mute 应译为“手掌制音”，原译“手掌护弦”不符合术语规范。 |
| 33415 | Slap Basics | 击打基础 | 拍弦基础 | B | 根据已落地术语，Slap 应译为“拍弦”，原译“击打”不准确。 |
| 33416 | Pop Basics | 流行基础 | 勾拍基础 | B | 原文 Pop 指贝斯/吉他技法 Pop，对应术语“勾拍”，而非音乐风格“流行”。 |
| 33654 | Learn basic strumming patterns with the G Major{C} D Major{C} and A Major chords. | 学习使用 G 大调{C} D 大调{C} 和 A 大调和弦的基本扫弦模式。 | 学习使用 G 大三和弦{C} D 大三和弦{C} 和 A 大三和弦的基本扫弦模式。 | B | 原文 G Major/D Major/A Major chords 指具体和弦，规则8要求 major chord 译为大三和弦，原译“大调”混淆了调性与和弦种类。 |
| 33655 | Add some rhythm to your rhythm guitar playing with basic strumming patterns using the G Major{C} D Major{C} and A Major  | 使用 G 大调{C} D 大调{C} 和 A 大调和弦，用基本扫弦模式为你的节奏吉他演奏增添节奏感。 | 使用 G 大三和弦{C} D 大三和弦{C} 和 A 大三和弦，用基本扫弦模式为你的节奏吉他演奏增添节奏感。 | B | 原文 G Major/D Major/A Major chords 指大三和弦，现译误作大调 |
| 33656 | Further expand your chord vocabulary with barre chords you can slide up and down the neck{C} allowing you to play any ma | 通过可沿琴颈上下滑动的横按和弦，进一步扩展你的和弦词汇量{C}让你能够演奏任何大调三和弦。 | 通过可沿琴颈上下滑动的横按和弦，进一步扩展你的和弦词汇量{C}让你能够演奏任何大三和弦。 | B | 已落地术语规定 major chord=大三和弦，原译“大调三和弦”错误。 |
| 33657 | Expand your harmonic universe even further with more barre chord shapes{C} focusing on dominant 7 chords{C} minor chords | 通过更多横按和弦形状进一步扩展你的和声宇宙{C} 重点练习属七和弦{C} 小和弦{C} 和小七和弦。 | 通过更多横按和弦指型进一步扩展你的和声宇宙{C} 重点练习属七和弦{C} 小和弦{C} 和小七和弦。 | B | 根据规则9，chord shapes 应译为“指型”或“形状”，原译“形状”虽可接受但“指型”更符合吉他教学术语习惯，且 major chord 等已正确，此处主要修正 shapes 的术语一致性，但原译“形状”并非绝对错误，然而结合上下文“barre chord shapes”通常指“横按和弦指型 |
| 33670 | Learn how to get a muffled{C} thunkier sound with palm mutes{C} allowing you to vary the sound of your notes as you play | 学习如何通过手掌护弦获得{C}沉闷且厚重的声音{C}从而在演奏中变化音符的音色。 | 学习如何通过手掌制音获得{C}沉闷且厚重的声音{C}从而在演奏中变化音符的音色。 | B | 已落地术语规定 palm mute 译为“手掌制音”，现译“手掌护弦”不符合术语规范。 |
| 33671 | Learn how to combine palm mutes with double stops for a muted sound with some harmonic variety. | 学习如何将手掌护弦与双音结合，以获得带有和声变化的闷音效果。 | 学习如何将手掌制音与双音结合，以获得带有和声变化的闷音效果。 | B | 已落地术语 palm mute=手掌制音，原译“手掌护弦”错误 |
| 33672 | Learn how to combine palm mutes with power chords for that classic "chugga-chugga" sound. | 学习如何将手掌护弦与强力和弦结合，营造经典的“咚咚”声效。 | 学习如何将手掌制音与强力和弦结合，营造经典的“咚咚”声效。 | B | 术语错误，已落地术语规定 palm mute 应译为“手掌制音”，而非“手掌护弦”。 |
| 33711 | Learn how to get a muffled{C} thunkier sound with palm mutes{C} allowing you to vary the sound of your notes as you play | 学习如何通过手掌护弦获得{C}沉闷且厚重的声音{C}从而在演奏中变化音符的音色。 | 学习如何通过手掌制音获得{C}沉闷且厚重的声音{C}从而在演奏中变化音符的音色。 | B | 已落地术语规定 palm mute 译为“手掌制音”，现译“手掌护弦”错误。 |
| 33764 | "Bends 102" | “Bends 102” | “推弦 102” | B | Bends 在吉他教学中统一译为推弦，现译保留英文不符合术语规范 |
| 33772 | "Chords 301" | “和弦高阶 301” | “和弦 301” | B | 课程标题通常保留数字编号，Chords 译为“和弦”即可，无需添加“高阶”等原文没有的修饰词。 |
| 33786 | "Palm Mutes 101" | “Palm Mutes 101” | “手掌制音 101” | B | 已落地术语规定 palm mute 统一译为手掌制音，且标题中的通用技法名应翻译。 |
| 33787 | "Palm Mutes 102" | “手掌护弦 102” | “手掌制音 102” | B | 已落地术语规定 palm mute 统一译为手掌制音 |
| 33793 | "Slides 101" | “Slides 101” | “滑音 101” | B | 术语统一：slide 应译为“滑音”，且课程标题需翻译。 |
| 34187 | palm mutes | 手掌闷音 | 手掌制音 | B | 根据已落地术语，palm mute 统一译为“手掌制音”，原译“手掌闷音”不一致。 |
| 34195 | pop frethand mutes | 流行乐左手闷音 | 勾拍左手制音 | B | 根据规则5，Pop 应译为“勾拍”，而非“流行乐”；fret-hand mute 对应“左手制音” |
| 34216 | Slides | 滑弦 | 滑音 | B | 模型未提供理由，需复核 |
| 34221 | Frethand Mutes | 按弦手制音 | 左手制音 | B | 已落地术语规定 fret-hand mute 译为左手制音，现译“按弦手制音”不符合术语规范。 |
| 34230 | Pop Fret Hand Mutes | 流行乐左手制音 | 勾拍左手制音 | B | Pop 在贝斯技法中应译为“勾拍”，而非“流行乐”；Fret Hand Mute 对应“左手制音”。 |
| 34236 | Oblique Bends | Oblique Bends | 斜向推弦 | B | Oblique Bends 是吉他演奏技法，指非垂直方向的推弦，应译为中文技法名而非保留英文 |
| 34245 | Palm Mute Double Stops | 手掌护弦双音 | 手掌制音双音 | B | 根据已落地术语，palm mute 应译为“手掌制音”，而非“手掌护弦”。 |
| 34248 | Slides | 滑弦 | 滑音 | B | 已落地术语规定 slide=滑音，原译“滑弦”错误。 |
| 34256 | Frethand Mutes | 按弦手制音 | 左手制音 | B | 已落地术语规定 fret-hand mute 译为左手制音 |
| 34260 | Palm Mute Double Stops | 手掌护弦双音 | 手掌制音双音 | B | 术语 Palm Mute 应统一译为“手掌制音”，而非“手掌护弦”。 |
| 34322 | You ran into some arpeggios last time you played this song{C} and it sounded like you were super close to mastering them | 你上次演奏这首歌时遇到了一些分解和弦{C} 听起来你快要掌握它们了。演奏Hurtlin' Hurdles是磨练分解和弦技巧的一种令人兴奋的方式{C} 这样你这次演奏这首歌时就能更接近完美。 | 你上次演奏这首歌时遇到了一些琶音{C} 听起来你快要掌握它们了。演奏Hurtlin' Hurdles是磨练琶音技巧的一种令人兴奋的方式{C} 这样你这次演奏这首歌时就能更接近完美。 | B | 根据已落地术语，Arpeggio 应译为“琶音”，原译“分解和弦”不符合术语规范。 |
| 34324 | It sounds like you're really close to mastering the slides in this song{C} so you should definitely give Ninja Slide N a | 听起来你快要掌握这首歌里的滑弦了{C}所以一定要试试忍者滑弦N。它会让完善滑弦变得有趣{C}并且让你为在歌曲中完美演奏它们做好更充分的准备。 | 听起来你快要掌握这首歌里的滑弦了{C}所以一定要试试 Ninja Slide N。它会让完善滑弦变得有趣{C}并且让你为在歌曲中完美演奏它们做好更充分的准备。 | B | Ninja Slide N 是游戏内特定活动/任务名称，应保留英文专名，不应译为“忍者滑弦N” |
| 34326 | Argeggios can be a little hard to get just perfect. It sounds like you're super close to mastering them{C} so give Strin | Argeggios 可能有点难做到完美。听起来你离掌握它们非常接近了{C}所以不妨试试 String Skip Saloon。这是练习它们的绝佳方式{C}这样你这次在歌曲中就能完美演奏它们了。 | 琶音可能有点难做到完美。听起来你离掌握它们非常接近了{C}所以不妨试试 String Skip Saloon。这是练习它们的绝佳方式{C}这样你这次在歌曲中就能完美演奏它们了。 | B | 规则9要求 Arpeggio 统一译为“琶音”，原译“Argeggios”为拼写错误且未翻译，应修正为中文术语。 |
| 34387 | palm mutes | 手掌闷音 | 手掌制音 | B | 已落地术语规定 palm mute=手掌制音，原译“手掌闷音”错误。 |
| 34394 | slap frethand mutes | 击弦手闷音 | 左手制音 | B | 根据已落地术语，fret-hand mute 应译为“左手制音”，而非“击弦手闷音”。 |
| 34395 | pop frethand mutes | 流行乐左手闷音 | 勾拍左手制音 | B | 术语错误：pop 在贝斯技法中译为“勾拍”，而非“流行乐”；fret-hand mute 译为“左手制音”。 |
| 34446 | Palm Mute Double Stops | 手掌护弦双音 | 手掌制音双音 | B | 术语表规定 palm mute 应译为“手掌制音”，原译“手掌护弦”不符合既定术语。 |
| 34447 | Palm Mute Power Chords | 手掌护弦强力和弦 | 手掌制音强力和弦 | B | 术语统一：Palm Mute 应译为“手掌制音”，而非“手掌护弦”。 |
| 34507 | Slap and Pop | 击打与拨弹 | 拍弦与勾拍 | B | 根据已落地术语规则，Slap 应译为‘拍弦’，Pop 应译为‘勾拍’，原译‘击打与拨弹’不符合既定术语规范。 |
| 34531 | Palm Mute | 手掌闷音 | 手掌制音 | B | 已落地术语规定 palm mute=手掌制音，现译“手掌闷音”不符合术语规范。 |
| 34532 | Slap | 击打 | 拍弦 | B | 根据已落地术语，Slap 统一译为拍弦，现译击打不准确 |
| 34539 | Pop Fret Hand Mute | 流行按弦手制音 | 勾拍左手制音 | B | 根据规则5，Pop 应译为勾拍；根据已落地术语，fret-hand mute 应译为左手制音，原译“流行按弦手制音”错误。 |
| 34864 | 18. Scale Shape | 18. 音阶型 | 18. 音阶指型 | B | 已落地术语 Scale Shape 应译为“音阶指型”，原译“音阶型”缺少“指”字，不符合术语规范。 |
| 35009 | Stop Your Slide Later! | 稍后停止滑动！ | 稍后停止滑音！ | B | 术语统一：slide 在吉他技法中应译为“滑音”，而非“滑动”。 |
| 35010 | Slide Faster! | 滑动更快！ | 滑音更快！ | B | Slide 在吉他演奏语境下指滑音，而非物理滑动 |
| 35190 | Giant treasure masks let you play the same harmonic multiple times for major points. | 巨型宝藏面具让你可以多次演奏相同的和声以获得大量分数。 | 巨型宝藏面具让你可以多次演奏相同的泛音以获得大量分数。 | B | 规则5：harmonic 在吉他演奏中特指“泛音”，而非“和声”。 |
| 35286 | Phrygian Dom | 弗里吉亚属调 | 弗里吉亚属音阶 | B | 根据已落地术语，Phrygian Dominant 应译为“弗里吉亚属音阶”，原译“弗里吉亚属调”混淆了音阶与调性概念。 |
| 35287 | Phrygian Dominant | 弗里吉亚属调式 | 弗里吉亚属音阶 | B | 已落地术语规定Phrygian Dominant译为弗里吉亚属音阶 |
| 35302 | Downbeat | 强拍 | 正拍 | B | 根据规则7，downbeat 在拨弦教学中对应“正拍”，不宜机械译为“强拍”。 |
| 35305 | This is the rhythmic feel of the session{C} and it affects the behavior of the Session Mode band. It plays an important  | 这是即兴演奏的节奏感{C} 它会影响即兴演奏乐队的行为。它在定义你即兴演奏期间乐队的风格方面起着重要作用。 | 这是即兴演奏的节奏感{C}，它会影响即兴演奏乐队的行为。它在定义你即兴演奏期间乐队的风格方面起着重要作用。 | B | 模型未提供理由，需复核 |
| 35341 | Scales are the building blocks of music. In Session Mode{C} Scale Shapes are displayed to give you a frame work for lear | 音阶是音乐的基石。在即兴演奏模式中{C}会显示音阶形态，为你学习即兴演奏提供框架。 | 音阶是音乐的基石。在即兴演奏模式中{C}会显示音阶指型，为你学习即兴演奏提供框架。 | B | 术语统一：Scale Shape 应译为“音阶指型”，而非“音阶形态” |
| 35499 | Phrygian Dominant Funk | 弗里吉亚属音Funk | 弗里吉亚属音阶 Funk | B | 原文 'Phrygian Dominant' 为音阶名称，已落地术语规定译为“弗里吉亚属音阶”，现译漏译“音阶”导致术语不完整。 |
| 35981 | Check out [1] in the Chord Book | 查看 [1] 在和弦书中 | 查看和弦书中的 [1] | B | 模型未提供理由，需复核 |

### 桶 C（114）

| id | source | original | revised | 分类 | reason |
|---|---|---|---|---|---|
| 17529 | You've  earned your first Rocksmith Points{C} a measure of your skill as a guitar player. Every time you increase your s | 你获得了你的第一个Rocksmith Points{C}这是衡量你吉他演奏水平的指标。每次你在排练中提高歌曲得分{C}或完成一个Event{C}你都会获得更多Rocksmith Points并提升你的等级。更多的点数还能让你有机会在更大的V | 你获得了你的第一个 Rocksmith Points{C} 这是衡量你吉他演奏水平的指标。每次你在排练中提高歌曲得分{C} 或完成一个活动{C} 你都会获得更多 Rocksmith Points 并提升你的等级。更多的点数还能让你有机会在更 | C | 原译中“Event”未翻译为已落地术语“活动”，且占位符{C}后缺少必要空格，导致中英文混排不规范。 |
| 17778 | You didn't score enough points to complete the Event. | 你的得分不足以完成该事件。 | 你的得分不足以完成该活动。 | C | 根据已落地术语，event(活动)应译为活动，原译“事件”错误。 |
| 17798 | Rehearsing for Events will push your skills to the next level. Once you play a song in an Event{C} you'll need to score  | 为活动进行排练将把您的技能提升到下一个水平。一旦您在活动中演奏了一首歌曲{C}您需要在排练中获得更高的分数才能在下一场活动中演奏它。 | 为活动进行排练将把你的技能提升到下一个水平。一旦你在活动中演奏了一首歌曲{C} 你需要在排练中获得更高的分数才能在下一场活动中演奏它。 | C | 原译使用“您”不符合玩家用“你”的规则，且“Event”未统一译为“活动”，占位符后缺少空格。 |
| 17828 | Each song has a unique scoring target you'll need to reach in order to unlock the gear that makes up the authentic tone. | 每首歌曲都有一个独特的得分目标，你需要达到该目标才能解锁构成真实音色的装备。这个分数会在你演奏歌曲前后显示在得分条上。 | 每首歌曲都有一个独特的得分目标，你需要达到该目标才能解锁构成原曲音色的装备。这个分数会在你演奏歌曲前后显示在得分条上。 | C | 根据已落地术语，authentic tone 应译为“原曲音色”，原译“真实音色”不准确。 |
| 17903 | Score 100{C}000 points in Rehearse Mode to play this song in Master Mode and earn double points! | 得分 100{C}在排练模式中得分 000 分，即可在大师模式中演奏此曲并获得双倍分数！ | 在排练模式中得分 100{C}000 分，即可在大师模式中演奏此曲并获得双倍分数！ | C | 原译“得分 100{C}在排练模式中得分 000 分”严重错误，将数字 100,000 拆分并插入了中文，导致语义完全混乱。原文是 Score 100{C}000 points，即 100,000 分。 |
| 21128 | This item is a component of a locked Authentic Tone. To unlock Authentic Tones and their components{C} reach the Tone Un | 此项目是锁定真实音色的组件。要解锁真实音色及其组件{C} 请达到歌曲计分条上列出的音色解锁分数目标。 | 此项目是锁定原曲音色的组件。要解锁原曲音色及其组件{C} 请达到歌曲计分条上列出的音色解锁分数目标。 | C | 根据已落地术语，Authentic Tone 应统一译为“原曲音色”，现译“真实音色”不符合术语规范。 |
| 21132 | Load an Authentic Tone you've unlocked{C} or a Custom Tone you've created.{L}{L}To unlock Authentic Tones{C} score above | 加载已解锁的真实音色{C}或已创建的自定义音色。{L}{L}要解锁真实音色{C}需在得分条上列出的每个编曲的音色解锁阈值以上得分。 | 加载已解锁的原曲音色{C}或已创建的自定义音色。{L}{L}要解锁原曲音色{C}需在得分条上列出的每个编曲的音色解锁阈值以上得分。 | C | 根据术语表，'Authentic Tone' 应译为 '原曲音色'，现译 '真实音色' 不符合已落地术语。 |
| 21776 | Beat 10{C}000{C}000 points in the Guitarcade game: Ducks | Beat 10{C}000{C}000 分在 Guitarcade 游戏：Ducks 中 | 在 Guitarcade 游戏：Ducks 中得分超过 10{C}000{C}000 分 | C | 原文 'Beat ... points' 意为得分超过某数值，现译 'Beat ... 分' 未翻译动词且语序混乱，需修正为中文自然表达并保留占位符。 |
| 21780 | Beat 150{C}000{C}000 points in the Guitarcade game: Super Ducks | 在{C}150{C}000 分在吉他街机游戏：超级鸭子中 | 在吉他街机游戏：超级鸭子中达到 150{C}000{C}000 分 | C | 现译 '在{C}150{C}000 分在吉他街机游戏：超级鸭子中' 语序完全错误，将分数和地点状语位置颠倒，且 'Beat ... points' 应译为 '达到/超过 ... 分'，现译结构混乱。 |
| 21788 | Beat 1{C}00{C}000 points in the Guitarcade game: Harmonically Challenged | Beat 1{C}00{C}000 分在 Guitarcade 游戏：Harmonically Challenged 中 | 在 Guitarcade 游戏：Harmonically Challenged 中击败 1{C}00{C}000 分 | C | 原译语序混乱，'Beat' 应译为 '击败' 并置于分数前，且 'in the ... game' 应前置为状语。 |
| 21800 | Beat 5{C}000{C}000 points in the Guitarcade game: Quick Pick Dash | Beat 5{C}000{C}000 分在 Guitarcade 游戏：Quick Pick Dash 中 | 在 Guitarcade 游戏：Quick Pick Dash 中得分超过 5{C}000{C}000 分 | C | 原译语序混乱且未体现 'Beat' (超过/打破) 的比较关系，导致任务条件不明确。 |
| 21804 | Beat 1{C}000{C}000 points in the Guitarcade game: Dawn of the Chordead | 在吉他街机游戏《Dawn of the Chordead》中{C}获得 100000{C}分 | 在 Guitarcade 游戏：Dawn of the Chordead 中得分超过 1{C}000{C}000 分 | C | 原译将占位符 {C} 错误地嵌入数字内部（100000{C}分），且未体现 'Beat' (超过) 的比较关系，导致数值显示错误且条件缺失。 |
| 21856 | Beat a 5-chord streak | Beat a 5-chord streak | 达成 5 连击和弦 | C | 原文 'Beat a 5-chord streak' 意为打破/达成 5 个和弦的连击记录，现译未翻译且 'Beat' 在此语境下应译为达成或打破记录，'streak' 对应连击。 |
| 21866 | Beat 200{C}000 points in Master Mode | 在{C}大师模式中获得 200000 分 | 在大师模式中获得 200{C}000 分 | C | 原译将占位符 {C} 错误地置于 '在' 和 '大师模式' 之间，且丢失了数字中的千位分隔符占位符，导致显示为 '在{C}大师模式中获得 200000 分'，应恢复为 '在大师模式中获得 200{C}000 分'。 |
| 22345 | You've earned your first Rocksmith Points{C} a measure of your skill as a bassist. Every time you increase your song sco | 你获得了你的第一笔 Rocksmith 点数{C}这是衡量你贝斯手技巧的标准。每次你在排练中提高歌曲得分{C}或完成一个事件{C}你都会获得更多 Rocksmith 点数并提升你的等级。更多的点数还能让你有机会在更大的场地面对更多观众进行演 | 你获得了你的第一笔 Rocksmith 点数{C}这是衡量你贝斯手技巧的标准。每次你在排练中提高歌曲得分{C}或完成一个活动{C}你都会获得更多 Rocksmith 点数并提升你的等级。更多的点数还能让你有机会在更大的场地面对更多观众进行演 | C | 根据已落地术语，'Event' 应译为“活动”而非“事件”。 |
| 22556 | Beat 100{C}000 points in a Bass arrangement | Beat 100{C}000 分在贝斯编曲中 | 在贝斯编曲中得分超过 100{C}000 分 | C | 原译“Beat”未翻译且语序错误，应译为“得分超过”并调整语序。 |
| 24165 | You can also explore over 300 existing Authentic Tones. | 你还可以探索超过 300 种现有的真实音色。 | 你还可以探索超过 300 种现有的原曲音色。 | C | 根据已落地术语，Authentic Tone 应译为“原曲音色”，原译“真实音色”不符合术语规范。 |
| 26965 | Successfully hit a palm mute. | 成功演奏了一个闷音。 | 成功演奏了一个手掌制音。 | C | 根据已落地术语，palm mute 应译为“手掌制音”，原译“闷音”不够精确。 |
| 27691 | Score at least [1] points in Hurtlin' Hurdles | 至少得分 [1] 分在 Hurtlin' Hurdles | 在 Hurtlin' Hurdles 中至少得分 [1] 分 | C | 原译“至少得分 [1] 分在 Hurtlin' Hurdles”语序错误，介词短语应前置。 |
| 27693 | Score [1] points in Harmonic Heist | 得分 [1] 分（Harmonic Heist） | 在 Harmonic Heist 中得分 [1] 分 | C | 原译“得分 [1] 分（Harmonic Heist）”括号用法不自然，调整为自然语序。 |
| 27695 | Score [1] points in Scale Racer | 得分 [1] 分于音阶竞速 | 在音阶竞速中得分 [1] 分 | C | 原译“得分 [1] 分于音阶竞速”语序生硬，调整为“在音阶竞速中得分 [1] 分”。 |
| 27701 | Score [1] points in Go Go Arpeggio! | 得分 [1] 分于 Go Go Arpeggio！ | 在 Go Go Arpeggio! 中得分 [1] 分。 | C | 原译“得分 [1] 分于 Go Go Arpeggio！”语序生硬，调整为自然中文语序。 |
| 27703 | Score [1] points in String Skip Saloon | 得分 [1] 分在 String Skip Saloon | 在 String Skip Saloon 中得分 [1] 分 | C | 原译“得分 [1] 分在 String Skip Saloon”语序错误，地点状语应前置，修正为“在 String Skip Saloon 中得分 [1] 分”。 |
| 27707 | Clear 30 songs on Score Attack Medium{C} Hard or Master | 在得分挑战中等难度下通关 30 首歌曲{C}或困难/大师难度 | 在得分挑战中等难度{C}困难或大师难度下通关 30 首歌曲 | C | 原译语序混乱，将“通关 30 首歌曲”这一核心动作后置且结构破碎，调整为“在...难度下通关 30 首歌曲”更符合中文逻辑。 |
| 27717 | Get Platinum on Score Attack Medium{C} Hard or Master | 在得分挑战中等难度获得白金{C}，或在困难或大师难度获得 | 在得分挑战中等难度{C}困难或大师难度获得白金 | C | 原译将占位符 {C} 错误地置于句尾，且断句逻辑混乱，导致“获得白金”的宾语缺失或语序不通，需调整语序以符合中文习惯并保留占位符位置。 |
| 29197 | Beat Chapter [1] in Return to Castle Chordead. | 击败章节 [1] 在《重返和弦城堡》中。 | 在《重返和弦城堡》中击败章节 [1]。 | C | 原译“击败章节 [1] 在《重返和弦城堡》中”语序错误，调整为状语前置。 |
| 29199 | Beat Chapter [1] in Scale Warriors. | 在《Scale Warriors》中[1]击败第 章。 | 在《Scale Warriors》中击败第 [1] 章。 | C | 原译“[1]击败第 章”占位符位置错误且缺失量词，导致语义不通，修正为“击败第 [1] 章”。 |
| 32028 | Shoot [1] ducks in a single game. | 射击 [1] 只鸭子（单局内）。 | 在一局游戏中射击 [1] 只鸭子。 | C | 原译“射击 [1] 只鸭子（单局内）”括号用法不自然，调整为自然语序。 |
| 32031 | Shoot [1] [2] ducks in a single game. | 击中 [1] [2] 只鸭子在一局游戏中。 | 在一局游戏中击中 [1] [2] 只鸭子。 | C | 原译语序生硬，调整以符合中文自然表达，同时保留占位符。 |
| 32036 | Shoot [1] ducks right before they hit the wall. | 射击 [1] 只鸭子，在它们撞上墙壁前。 | 在鸭子撞上墙壁前射击 [1] 只鸭子。 | C | 原译将时间状语“在它们撞上墙壁前”后置，导致中文表达生硬，调整语序使条件前置更符合中文任务描述习惯。 |
| 32046 | Score a x[1] multiplier. | 得分 [1] 倍率。 | 获得 [1] 倍得分。 | C | 原文 'Score a x[1] multiplier' 意为达成 x[1] 的倍率，现译 '得分 [1] 倍率' 语序不通且未体现动作，应译为 '获得 [1] 倍得分' 或 '达成 [1] 倍率'。 |
| 32050 | Collect [1] golden bolts in a single game. | 收集 [1] 颗金色螺栓，在一局游戏中。 | 在一局游戏中收集 [1] 颗金色螺栓。 | C | 原译“收集 [1] 颗金色螺栓，在一局游戏中”语序生硬，调整为自然中文语序。 |
| 32061 | Collect [1] batteries in a single game. | 收集 [1] 电池于一局游戏中。 | 在一局游戏中收集 [1] 个电池。 | C | 原译语序生硬，调整以符合中文自然表达，同时保留占位符。 |
| 32069 | Collect [1] golden bolts. | 收集 [1] 金色螺栓。 | 收集 [1] 个金色螺栓。 | C | 原译“收集 [1] 金色螺栓”缺少量词“个”，中文中数量词后通常需接量词，补全后更规范。 |
| 32073 | Leap [1] hurdles in a row. | 连续跳跃 [1] 次。 | 连续跳过 [1] 个障碍。 | C | 原译“连续跳跃 [1] 次”丢失了“hurdles”（障碍）这一关键对象，且“跳跃”不如“跳过”准确描述跨越障碍的动作。 |
| 32074 | Leap [1] hurdles. | 跳过 [1] 障碍。 | 跳过 [1] 个障碍。 | C | 原译“跳过 [1] 障碍”缺少量词，补充“个”使表达完整。 |
| 32075 | Collect [1] golden bolts in a single game. | 收集 [1] 颗金色螺栓，在一局游戏中。 | 在一局游戏中收集 [1] 颗金色螺栓。 | C | 原译“收集 [1] 颗金色螺栓，在一局游戏中。”语序生硬，调整为自然语序。 |
| 32077 | Collect [1] golden bolts. | 收集 [1] 金色螺栓。 | 收集 [1] 个金色螺栓。 | C | 原译缺少量词“个”，中文表达不完整，需补充量词以符合语法规范。 |
| 32084 | Collect [1] batteries from the battery bot. | 收集 [1] 节电池，来自电池机器人。 | 从电池机器人处收集 [1] 节电池。 | C | 原译“来自电池机器人”不符合中文任务指令习惯，调整为“从...处收集”。 |
| 32104 | Touch [1] islands in a single game. | 在单局游戏中触碰 [1] 座岛屿。 | 在一局游戏中触碰 [1] 座岛屿。 | C | 原译“在单局游戏中触碰 [1] 座岛屿”中“单局”可接受，但“一局”更通用，且原译语序已自然，保留原意微调为更自然的“一局”。 |
| 32117 | Avoid touching [1] islands in a row. | 避免触碰[1]连续出现的岛屿。 | 避免连续触碰 [1] 个岛屿。 | C | 原文 'Avoid touching [1] islands in a row' 意为避免连续触碰 [1] 个岛屿，原译“避免触碰[1]连续出现的岛屿”语义略有偏差，调整为更准确的表达。 |
| 32122 | Avoid [1] banana chains in a row. | 避免[1]连续出现香蕉链。 | 避免连续出现 [1] 次香蕉链。 | C | 原文 'Avoid [1] banana chains in a row' 意为避免连续出现 [1] 个/次香蕉链，现译 '避免[1]连续出现香蕉链' 语序不当，[1] 应修饰次数或数量，且 'in a row' 对应连续。 |
| 32128 | Collect only the first banana in a chain [1] times in a single game. | 仅收集连击中的第一根香蕉[1]次于一局游戏中。 | 在一局游戏中，仅收集连击中的第一根香蕉 [1] 次。 | C | 原译“仅收集连击中的第一根香蕉[1]次于一局游戏中”语序混乱，调整语序并明确条件。 |
| 32136 | Score a x[1] multiplier. | 得分 [1] 倍率。 | 获得 [1] 倍率。 | C | 原文 Score a x[1] multiplier 意为达成/获得该倍率，现译“得分 [1] 倍率”动宾搭配不当且语义模糊。 |
| 32141 | Destroy [1] long platforms with the shredder fan in a single game. | 摧毁 [1] 个长平台（使用粉碎风扇），在一局游戏中完成。 | 在一局游戏中使用粉碎风扇摧毁 [1] 个长平台。 | C | 原译括号注释不符合游戏成就文本规范，且语序不佳，调整为自然中文状语前置。 |
| 32146 | Destroy [1] platforms with the shredder fan in a single game. | 摧毁 [1] 个平台，使用粉碎风扇于一局游戏中。 | 在一局游戏中使用粉碎风扇摧毁 [1] 个平台。 | C | 原译语序生硬，调整以符合中文自然表达，同时保留占位符和关键术语。 |
| 32148 | Destroy [1] zap platforms with the shredder fan without jumping on them in a single game. | 摧毁 [1] 个电击平台，使用粉碎风扇且不跳上它们于一局游戏中。 | 在一局游戏中，使用粉碎风扇摧毁 [1] 个电击平台，且不跳上它们。 | C | 原译语序混乱，“使用粉碎风扇且不跳上它们于一局游戏中”不符合中文语法，需调整状语位置以清晰表达条件与动作。 |
| 32159 | Destroy [1] platforms with the shredder fan. | 摧毁 [1] 个平台，使用粉碎风扇。 | 使用粉碎风扇摧毁 [1] 个平台。 | C | 原译“摧毁 [1] 个平台，使用粉碎风扇。”语序略显生硬，但主要问题是“shredder fan”译为“粉碎风扇”可能不准确，但在游戏语境下通常指“碎纸机风扇”或类似机制。若“shredder”指碎纸机，则“粉碎风扇”可接受。原译语序“摧毁...，使用...”是中文常见结构，不算错误。但对比其他条目 |
| 32180 | Steal treasures from the 5th{C} 7th{C} and 12th frets in a single game. | 从第5{C} 7{C} 和12品偷取宝藏，于一局游戏中。 | 在一局游戏中从第5{C} 7{C} 和12品偷取宝藏。 | C | 现译“...于一局游戏中”语序不符合中文习惯，应调整为状语前置。 |
| 32181 | Steal [1] treasures in a single game. | 偷取 [1] 一局游戏中的宝藏。 | 在一局游戏中偷取 [1] 件宝藏。 | C | 语序与量词：原译“偷取 [1] 一局游戏中的宝藏”语序混乱且缺少量词，应调整为“在一局游戏中偷取 [1] 件宝藏”。 |
| 32184 | Steal [1] [2] treasures in a single game. | 偷取 [1] [2] 件宝物，仅限单局游戏。 | 在一局游戏中偷取 [1] [2] 件宝物。 | C | 原译“仅限单局游戏”语序生硬，调整为更自然的中文任务描述结构，同时保留“一局游戏”这一已落地术语。 |
| 32186 | Steal [1] treasures in a row{C} in a single game. | 偷取 [1] 件宝藏，连续{C} 次，在一局游戏内。 | 在一局游戏内连续偷取 [1] 件宝藏{C}。 | C | 原译“偷取 [1] 件宝藏，连续{C} 次，在一局游戏内”语序破碎，调整为通顺的中文表达。 |
| 32191 | Steal [1] treasures from exposed pedestals in a single game. | 偷取 [1] 件宝藏，从暴露的基座上，在一局游戏内。 | 在一局游戏内从暴露的基座上偷取 [1] 件宝藏。 | C | 现译 '偷取 [1] 件宝藏，从暴露的基座上，在一局游戏内' 语序混乱，不符合中文表达习惯，且 '从...上' 作为状语后置显得生硬，应调整语序使句子通顺。 |
| 32192 | Steal [1] treasures in a row from exposed pedestals. | 偷取[1] 件宝藏，从暴露的基座上连续获取。 | 从暴露的基座上连续偷取 [1] 件宝藏。 | C | 原译“偷取[1] 件宝藏，从暴露的基座上连续获取。”语序混乱且“连续获取”与“偷取”重复。原文是 Steal [1] treasures in a row from exposed pedestals，即“从暴露的基座上连续偷取 [1] 件宝藏”。 |
| 32193 | Steal [1] treasures in a row. | 偷取 [1] 件宝藏，连续不断。 | 连续偷取 [1] 件宝藏。 | C | 原译“偷取 [1] 件宝藏，连续不断”语序生硬，in a row 应译为连续，修饰动作。 |
| 32194 | Steal [1] treasures from exposed pedestals. | 偷取 [1] 暴露在外的基座上的宝藏。 | 从暴露的基座上偷取 [1] 件宝藏。 | C | 原译“偷取 [1] 暴露在外的基座上的宝藏”量词“个”用于宝藏不当，改为“件”并调整语序。 |
| 32195 | Score [1] multipliers in a single game. | 得分 [1] 倍率在一局游戏中。 | 在一局游戏中获得 [1] 个倍率。 | C | 原文 Score [1] multipliers 意为获得倍率，现译“得分...倍率”动宾搭配错误且语序混乱。 |
| 32196 | Score a multiplier [1] times. | 获得 [1] 倍乘数。 | 获得 [1] 次乘数奖励。 | C | 原译“获得 [1] 倍乘数”语义不通，Score a multiplier [1] times 意为触发/获得乘数效果 [1] 次，而非获得 [1] 倍的乘数。 |
| 32197 | Steal [1] green emeralds in a single game. | 偷取 [1] 颗绿色祖母绿于一局游戏中。 | 在一局游戏中偷取 [1] 颗绿色祖母绿。 | C | 模型未提供理由，需复核 |
| 32200 | Steal [1] purple cat statues in a single game. | 偷取 [1] 尊紫色猫雕像于一局游戏中。 | 在一局游戏中偷取 [1] 尊紫色猫雕像。 | C | 现译“偷取...于一局游戏中”语序不符合中文习惯，应调整为状语前置。 |
| 32202 | Steal [1] yellow busts in a single game. | 偷取 [1] 一局游戏中的黄色半身像。 | 在一局游戏中偷取 [1] 个黄色半身像。 | C | 原译“偷取 [1] 一局游戏中的黄色半身像”语序混乱，导致 [1] 修饰对象不明，应调整为“在一局游戏中偷取 [1] 个...”以符合中文逻辑。 |
| 32203 | Steal [1] green emeralds and [2] jewels from giant treasure masks a single game. | 偷走 [1] 颗绿色祖母绿和 [2] 颗宝石，目标是一局游戏中的巨型宝藏面具。 | 在一局游戏中从巨型宝藏面具处偷走 [1] 颗绿色祖母绿和 [2] 颗宝石。 | C | 原译“目标是一局游戏中的巨型宝藏面具”严重误译，source 意为“从...面具处偷取”，且“a single game”是时间状语。 |
| 32204 | Steal [1] orange crowns and [2] jewels from giant treasure masks a single game. | 偷取 [1] 顶橙色皇冠和 [2] 颗宝石，来自巨型宝藏面具，于一局游戏中。 | 在一局游戏中，从巨型宝藏面具上偷取 [1] 顶橙色皇冠和 [2] 颗宝石。 | C | 模型未提供理由，需复核 |
| 32205 | Steal [1] blue necklaces and [2] jewels from giant treasure masks a single game. | 偷走 [1] 条蓝色项链和 [2] 颗宝石，来自一局游戏中的巨型宝藏面具。 | 在一局游戏中，从巨型宝藏面具上偷走 [1] 条蓝色项链和 [2] 颗宝石。 | C | 原译“来自一局游戏中的巨型宝藏面具”语序混乱，未能准确表达“from giant treasure masks”作为来源状语修饰“Steal”的逻辑关系，且“a single game”应译为“一局游戏中”以符合任务条件语境。 |
| 32206 | Steal [1] purple cat statues and [2] jewels from giant treasure masks a single game. | 偷取[1] 个紫色猫雕像和[2] 颗宝石，从巨大的宝藏面具上，在一局游戏中。 | 在一局游戏中，从巨大的宝藏面具上偷取 [1] 个紫色猫雕像和 [2] 颗宝石。 | C | 模型未提供理由，需复核 |
| 32207 | Steal [1] red urns and [2] jewels from giant treasure masks in a single game. | 偷取 [1] 红色瓮和 [2] 一局游戏中巨型宝藏面具上的宝石。 | 在一局游戏中从巨型宝藏面具上偷取 [1] 个红色瓮和 [2] 颗宝石。 | C | 原译“偷取 [1] 红色瓮和 [2] 一局游戏中巨型宝藏面具上的宝石。”语序混乱，将“一局游戏中”插入到宾语中间，导致句子结构破碎。应调整为“在一局游戏中从...偷取...”。 |
| 32208 | Steal [1] yellow busts and [2] jewels from giant treasure masks in a single game. | 偷取 [1] 个黄色半身像和 [2] 颗宝石，从巨型宝藏面具中，在一局游戏内。 | 在一局游戏内，从巨型宝藏面具中偷取 [1] 个黄色半身像和 [2] 颗宝石。 | C | 原译语序混乱，将状语“在一局游戏内”后置导致中文表达不自然且逻辑割裂，调整语序以符合中文习惯并保留所有条件。 |
| 32210 | Steal [1] orange crowns and [2] [3] jewels from a giant treasure mask. | 偷取[1] 个橙色王冠和[2] [3] 颗宝石，从巨大的宝藏面具上。 | 从巨大的宝藏面具上偷取 [1] 个橙色王冠和 [2] [3] 颗宝石。 | C | 原译“偷取...从巨大的宝藏面具上”语序生硬，调整为状语前置。 |
| 32211 | Steal [1] blue necklaces and [2] [3] jewels from a giant treasure mask. | 偷走 [1] 条蓝色项链和 [2] [3] 颗宝石，目标是一个巨型宝藏面具。 | 从巨型宝藏面具上偷走 [1] 条蓝色项链和 [2] [3] 颗宝石。 | C | 原译“目标是一个巨型宝藏面具”改变了原意，原文是“from a giant treasure mask”（从...上），表示来源，而非目标。且原译语序混乱。 |
| 32212 | Steal [1] purple cat statues and [2] [3] jewels from a giant treasure mask. | 偷取 [1] 紫色猫雕像和 [2] [3] 巨型宝藏面具上的宝石。 | 从巨型宝藏面具处偷取 [1] 紫色猫雕像和 [2] [3] 宝石。 | C | 原译“偷取 [1] 紫色猫雕像和 [2] [3] 巨型宝藏面具上的宝石”结构混乱，source 意为从面具处偷取两类物品。 |
| 32213 | Steal [1] red urns and [2] [3] jewels from a giant treasure mask. | 偷取 [1] 个红色瓮和 [2] [3] 颗宝石，从巨型宝藏面具中。 | 从巨型宝藏面具中偷取 [1] 个红色瓮和 [2] [3] 颗宝石。 | C | 原译语序混乱，'from a giant treasure mask' 是地点状语，应前置或后置使句子通顺，现译 '从巨型宝藏面具中' 悬空在句末不符合中文习惯。 |
| 32244 | Play [1] perfect slides on the yellow string in a single game. | 弹奏 [1] 个黄色琴弦上的完美滑弦于一局游戏中。 | 在一局游戏中，在黄色琴弦上弹奏 [1] 个完美滑弦。 | C | 现译 '弹奏 [1] 个黄色琴弦上的完美滑弦于一局游戏中' 语序生硬，'于一局游戏中' 后置不符合中文习惯，调整为 '在一局游戏中，在黄色琴弦上弹奏 [1] 个完美滑弦' 更自然且保留所有条件。 |
| 32250 | Play [1] perfect slides on the green string in a single game. | 弹奏 [1] 个绿色琴弦上的完美滑弦于一局游戏中。 | 在一局游戏中，在绿色琴弦上弹奏 [1] 个完美滑音。 | C | 原译语序生硬且不符合中文习惯，'弹奏...于一局游戏中' 结构错误，调整为自然语序。 |
| 32254 | Slice [1] ghosts in a single game. | 切 [1] 个幽灵于一局游戏中。 | 在一局游戏中切 [1] 个幽灵。 | C | 原译“切 [1] 个幽灵于一局游戏中”语序生硬，调整为自然状语前置。 |
| 32265 | Play [1] perfect slides in a row. | 演奏 [1] 次完美滑音。 | 连续演奏 [1] 次完美滑音。 | C | 原文是 in a row，意为“连续”，原译“演奏 [1] 次完美滑音。”漏掉了“连续”这一关键条件。 |
| 32271 | Slide to [1] towers in a single game. | 滑向[1]单局游戏中的塔楼。 | 在一局游戏中滑向 [1] 座塔楼。 | C | 原译“滑向[1]单局游戏中的塔楼”语序混乱，导致“单局游戏”被错误地修饰“塔楼”，且缺少量词，应调整为“在一局游戏中滑向 [1] 座塔楼”以符合中文语法及任务条件表述。 |
| 32300 | Pass [1] consecutive lines of cars in a single game. | 连续通过[1]条车道中的车辆。 | 在一局游戏中连续通过[1]条车道的车辆。 | C | 原译“连续通过[1]条车道中的车辆”语意模糊，易误解为在单条车道内连续通过车辆；原意应为跨越/通过[1]条不同车道的车辆。 |
| 32366 | Score [1] points in a single game. | 得分 [1] 分（单局游戏）。 | 在单局游戏中得分 [1] 分。 | C | 原译“得分 [1] 分（单局游戏）”使用括号表达条件不够自然，调整为“在单局游戏中得分 [1] 分”。 |
| 32381 | Score [1] quick-draw bonuses in a single game. | 得分 [1] 快速拔枪奖励在一局游戏中。 | 在一局游戏中获得 [1] 个快速拔枪奖励。 | C | 原译“得分 [1] 快速拔枪奖励在一局游戏中”语序错误，将时间/范围状语后置导致句意不通，且“Score”在此处作动词应译为“获得”或“取得”以搭配“奖励”。 |
| 32385 | Score [1] quick-draw bonuses in a row. | 得分 [1] 次连续快速反应奖励。 | 连续获得 [1] 次快速反应奖励。 | C | 原译“得分 [1] 次连续快速反应奖励”语序混乱且不符合中文习惯，in a row 应译为连续，quick-draw bonuses 为奖励。 |
| 32391 | Score a quick-draw bonus on [1] front-runner bandits in a single game. | 对 [1] 名领先强盗获得快速反应奖励。 | 在一局游戏中，对 [1] 名领先强盗获得快速反应奖励。 | C | 原译漏译了关键条件 'in a single game' (在一局游戏中)，导致任务条件缺失。 |
| 32394 | Score [1] quick-draw bonuses. | 得分 [1] 次速射奖励。 | 获得 [1] 次速射奖励。 | C | 模型未提供理由，需复核 |
| 32395 | Shoot down [1] front-runner bandits. | 击落 [1] 个领跑强盗。 | 击落 [1] 名领跑强盗。 | C | 原文 'front-runner' 意为 '领跑者'，现译 '领跑强盗' 可接受，但量词 '个' 用于人时 '名' 更规范，且 'front-runner' 在 Rocksmith 语境下通常指 '领跑' 状态或角色，此处修正量词。 |
| 32396 | Shoot down [1] of every bandit color in a single game. | 击落 [1] 名每种颜色的强盗，在一局游戏中。 | 在一局游戏中击落每种颜色的 [1] 名强盗。 | C | 原译语序“在一局游戏中”后置导致句子结构松散，且“击落 [1] 名每种颜色的强盗”易产生歧义，调整为“在一局游戏中击落每种颜色的 [1] 名强盗”更符合中文习惯且保留条件。 |
| 32399 | Shoot down [1] front-runner bandits in a single game. | 击落 [1] 名领头强盗（单局内）。 | 在一局游戏中击落 [1] 名领头强盗。 | C | 原译“（单局内）”括号用法不符合游戏成就描述规范，调整为自然状语。 |
| 32400 | Score [1] quick-draw bonuses in a single game. | 得分 [1] 快速拔枪奖励在一局游戏中。 | 在一局游戏中获得 [1] 个快速拔枪奖励。 | C | 原文 Score [1] quick-draw bonuses 意为获得奖励，现译“得分...奖励”动宾搭配错误且语序混乱。 |
| 32402 | Shoot [1] front-runner bandits in a row. | 射击 [1] 名连续领先的强盗。 | 连续射击 [1] 名领跑强盗。 | C | 原文 'in a row' 意为连续，现译 '连续领先' 语义错误且 'front-runner' 应译为 '领跑'。 |
| 32403 | Score [1] quick-draw bonuses in a row. | 得分 [1] 次连续快速反应奖励。 | 连续获得 [1] 次快速反应奖励。 | C | 原文 'Score [1] quick-draw bonuses in a row' 意为连续获得 [1] 次奖励，现译 '得分 [1] 次连续快速反应奖励' 语序混乱且 '得分' 误作动词修饰奖励，应调整为 '连续获得 [1] 次快速反应奖励' 以准确表达任务条件。 |
| 32404 | Score a quick-draw bonus on [1] front-runner bandits in a single game. | 对 [1] 名领先强盗获得快速反应奖励。 | 在一局游戏中对 [1] 名领先强盗获得快速反应奖励。 | C | 原译漏译了“in a single game”（在一局游戏中），这是任务的关键条件，必须补全。 |
| 32406 | Shoot down [1] [2] bandits in a single game. | 击落 [1] [2] 名强盗，在一局游戏中。 | 在一局游戏中击落 [1] [2] 名强盗。 | C | 现译语序略显生硬，调整为更自然的中文语序，保留所有占位符和条件。 |
| 32415 | Shoot consecutively between the top and bottom strings [1] times. | 在最高弦和最低弦之间连续射击 [1] 次。 | 在最高弦和最低弦之间连续拨弦 [1] 次。 | C | 原译“射击”不符合吉他演奏语境，应为“拨弦”或“弹奏”；此处指在弦间进行演奏动作。 |
| 33872 | You're pretty good{C} and you know you could be better. Challenge yourself to improve by beating this note streak! | 你表现得不错{C}而且你知道自己可以做得更好。挑战自己，打破这个连击纪录来提升水平！ | 你表现得不错{C}，而且你知道自己可以做得更好。挑战自己，打破这个连击纪录来提升水平！ | C | 原文 'You're pretty good{C} and you know...' 中 {C} 后紧跟 and，中文语境下 {C} 通常代表标点或连接符，若 {C} 为逗号或空格，现译 '不错{C}而且' 略显生硬，但更关键的是 'beat this note streak' 译为 '打破这个连击 |
| 34009 | Get a new high score in Score Attack on Easy for [1]. | 在得分挑战的简单难度中刷新最高分，达到 [1]。 | 在得分挑战的简单难度中刷新 [1] 的最高分。 | C | 原文 'Get a new high score in Score Attack on Easy for [1]' 中 [1] 是歌曲名。现译 '刷新最高分，达到 [1]' 将 [1] 误译为分数目标，实际 [1] 是歌曲。 |
| 34060 | Successfully hit 4 slides. | 成功弹奏 4 个滑音。 | 成功完成 4 个滑音。 | C | Slide 译为“滑音”，动词用“完成”比“弹奏”更准确描述技法达成。 |
| 34070 | Successfully hit 4 palm mutes. | 成功完成了 4 次手掌闷音。 | 成功完成了 4 次手掌制音。 | C | 根据术语表，'palm mute' 应译为 '手掌制音'，现译 '手掌闷音' 不符合已落地术语。 |
| 34073 | Successfully hit 4 frethand mutes. | 成功完成了 4 次左手闷音。 | 成功完成了 4 次左手制音。 | C | 已落地术语规定 fret-hand mute 应译为“左手制音”，原译“左手闷音”不符合术语规范。 |
| 34075 | Successfully hit 4 chords. | 成功击中 4 个和弦。 | 成功演奏 4 个和弦。 | C | 原文 'hit' 在吉他演奏语境下指弹奏/演奏，现译 '击中' 为误译，应改为 '演奏'。 |
| 34099 | Successfully hit a chord frethand mute. | 成功完成了一次和弦左手闷音。 | 成功完成了一次和弦左手制音。 | C | 已落地术语规定 fret-hand mute=左手制音，原译“左手闷音”不符合术语规范。 |
| 34100 | Successfully hit 4 A chords. | 成功弹奏了 4 个 A 和弦。 | 成功弹奏 4 个 A 和弦。 | C | 原译“成功弹奏了 4 个 A 和弦”中“了”字多余，任务描述通常用一般现在时或祈使语气，去掉“了”更简洁。 |
| 34109 | Successfully hit 4 chord frethand mutes. | 成功弹奏 4 个和弦制音。 | 成功弹奏 4 个和弦左手制音。 | C | 术语规范：fret-hand mute 应译为“左手制音”，现译“和弦制音”不准确且未体现手指部位。 |
| 34110 | Successfully hit 4 chord palm mutes. | 成功演奏了 4 个和弦闷音。 | 成功演奏 4 个和弦手掌制音。 | C | 根据已落地术语，palm mute 应译为“手掌制音”，原译“闷音”不准确。 |
| 34122 | Successfully hit 4 chord slides. | 成功完成了 4 次和弦滑音。 | 成功演奏 4 个和弦滑音。 | C | 原译“完成了 4 次”不如“演奏 4 个”准确，slide 为滑音，用“演奏”更贴切。 |
| 34132 | Successfully hit a slap. | 成功完成了一次击弦。 | 成功完成了一次拍弦。 | C | 根据已落地术语，Slap 应译为“拍弦”，原译“击弦”不准确。 |
| 34134 | Successfully hit a slap frethand mute. | 成功演奏了击弦手闷音。 | 成功演奏了拍弦左手制音。 | C | 根据术语表，Slap 应译为 '拍弦'，fret-hand mute 应译为 '左手制音'，原译 '击弦手闷音' 错误。 |
| 34135 | Successfully hit a pop frethand mute. | 成功完成了一次 Pop 左手闷音。 | 成功演奏了勾拍左手制音。 | C | 根据术语表，Pop 应译为 '勾拍'，fret-hand mute 应译为 '左手制音'，原译 'Pop 左手闷音' 错误。 |
| 34136 | Successfully hit 4 slaps. | 成功完成了 4 次击弦。 | 成功完成了 4 次拍弦。 | C | 根据术语表，Slap 应译为 '拍弦'，原译 '击弦' 错误。 |
| 34137 | Successfully hit 4 pops. | 成功击中 4 个波普。 | 成功完成 4 个勾拍。 | C | Pop 在贝斯/吉他技法中应译为“勾拍”，而非“波普”或“击中”。 |
| 34138 | Successfully hit 4 slap frethand mutes. | 成功完成 4 次击弦手闷音。 | 成功完成 4 次拍弦左手制音。 | C | slap 对应“拍弦”，fret-hand mute 对应“左手制音”，原译“击弦手闷音”术语错误。 |
| 34139 | Successfully hit 4 pop frethand mutes. | 成功演奏了 4 个流行乐左手闷音。 | 成功演奏了 4 个勾拍左手制音。 | C | 原文 'pop' 在吉他技法中指 '勾拍' (Pop)，现译 '流行乐' 为误译；'fret-hand mute' 对应 '左手制音'。 |
| 34969 | Beat your previous best. | Beat your previous best. | 超越你的最佳成绩。 | C | 原译未翻译，需译为中文。 |
| 35000 | Steal [1] treasures from a single giant treasure mask. | 偷取 [1] 件宝藏，来自单个巨型宝藏面具。 | 从单个巨型宝藏面具处偷取 [1] 件宝藏。 | C | 原译“偷取 [1] 件宝藏，来自单个巨型宝藏面具”语序生硬，调整为“从...处偷取...”更符合中文表达习惯且保留所有条件。 |
| 35139 | Shielded Ships Destroyed | Shielded Ships Destroyed | 摧毁的护盾飞船 | C | 原文 Shielded Ships Destroyed 为成就/统计名称，需翻译为中文，现译保留英文违反规则18。 |
| 35227 | Improve your score by reaching a score of at least [1]. | 达到至少 {0} 的分数来提升你的得分。[1]。 | 达到至少 [1] 的分数来提升你的得分。 | C | 原译“达到至少 {0} 的分数来提升你的得分。[1]。”占位符错误，source 为 [1]，应替换为 [1] 并修正语序。 |
| 36063 | Score Attacking a Song | 得分：挑战歌曲 | 得分挑战：歌曲 | C | Score Attack 是固定术语，应译为“得分挑战”，原译“得分：挑战歌曲”割裂了术语且语意不通。 |

### 桶 D（83）

| id | source | original | revised | 分类 | reason |
|---|---|---|---|---|---|
| 5879 | Cannot join a ranked match in progress. | 无法加入正在进行的排位赛。 | 无法加入正在进行的排位对局。 | D | 根据术语表，match 应统一译为“对局”，现译“排位赛”虽可接受但“排位对局”更贴合游戏内 match 的通用译法，且避免与体育比赛混淆。 |
| 5911 | Your NAT type is STRICT. You may not be able to join certain games or communicate with other players. Average matchmakin | 你的 NAT 类型为 STRICT。你可能无法加入某些游戏或与其他玩家通信。平均匹配等待时间会受到不利影响。 | 你的 NAT 类型为严格。你可能无法加入某些游戏或与其他玩家通信。平均匹配等待时间会受到不利影响。 | D | NAT 类型 STRICT 应译为“严格”以对应中文语境，原译保留英文不符合本地化规范 |
| 5974 | Some or all of your downloadable content requires a Title Update from Xbox LIVE. You will not be able to access it until | 部分或全部下载内容需要 Xbox LIVE 的游戏更新。在应用更新之前，你将无法访问这些内容。 | 部分或全部下载内容需要 Xbox LIVE 的标题更新。在应用标题更新之前，你将无法访问这些内容。 | D | 模型未提供理由，需复核 |
| 6017 | Your game experience will be satisfactory but you might encounter minor issues{C} especially if you use the voice chat.  | 您的游戏体验将令人满意，但可能会遇到一些小问题{C}尤其是使用语音聊天时。请限制网络流量以提升表现。 | 你的游戏体验将令人满意，但可能会遇到一些小问题{C}尤其是使用语音聊天时。请限制网络流量以提升表现。 | D | 统一使用“你”作为玩家代词，原译“您”不符合规则5及本桶重点要求 |
| 6023 | Your game experience will be satisfactory but you might encounter minor issues{C} especially if you use the voice chat.  | 您的游戏体验将令人满意，但可能会遇到一些小问题{C}尤其是使用语音聊天时。请限制网络流量以提升表现。 | 你的游戏体验将令人满意，但可能会遇到一些小问题{C}尤其是使用语音聊天时。请限制网络流量以提升表现。 | D | 根据规则5，玩家用你，原译 '您的' 不符合代词规则。 |
| 6077 | Activate your Uplay Passport to access online multiplayer. If your Uplay Passport code is missing{C} or it has already b | 激活你的 Uplay 护照以访问在线多人游戏。如果你的 Uplay 护照代码缺失{C}或已被兑换{C}你可以在 %s 中购买新的护照，或开始 %d 天免费试用。 | 激活你的 Uplay Passport 以访问在线多人游戏。如果你的 Uplay Passport 代码缺失{C}或已被兑换{C}你可以在 %s 中购买新的护照，或开始 %d 天免费试用。 | D | Uplay Passport 为品牌专名，保留英文；原译将 Passport 译为护照，违反品牌专名保留规则。 |
| 6476 | Activate your Uplay Passport to access online Multiplayer content without restrictions (without a Uplay Passport{C} you  | 激活你的 Uplay Passport 以无限制地访问在线多人内容（没有 Uplay Passport{C}你将无法购买能力{C}奖励{C}连击和 10 级以上的物品）。如果你的 Uplay Passport 代码缺失{C}或已被兑换{C} | 激活你的 Uplay Passport 以无限制地访问在线多人内容（没有 Uplay Passport{C}你将无法购买 10 级以上的能力{C}奖励{C}连击和物品）。如果你的 Uplay Passport 代码缺失{C}或已被兑换{C} | D | 原文 'abilities, perks, streaks and items past level 10' 中 'past level 10' 修饰整个列表，现译将 '10 级以上' 仅修饰 '物品'，导致语义范围错误。 |
| 6519 | The Xbox LIVE Marketplace cannot be reached at the moment. Please try again later or check your internet settings. | 目前无法连接 Xbox LIVE 市场。请稍后重试或检查您的互联网设置。 | 目前无法连接 Xbox LIVE 市场。请稍后重试或检查你的互联网设置。 | D | 统一使用“你”作为玩家代词，原译“您”不符合规则5及本桶重点要求 |
| 6520 | The GAME SESSION ended prematurely because of an insufficient number of PLAYERS. | 由于玩家人数不足，GAME SESSION 已提前结束。 | 由于玩家人数不足，游戏会话已提前结束。 | D | source 中 GAME SESSION 为通用游戏术语，非品牌专名，应译为“游戏会话”而非保留英文 |
| 6541 | Your Ethernet cable has been disconnected. Returning to Main Menu... | 你的以太网电缆已断开。正在返回主菜单... | 你的以太网电缆已断开。正在返回主菜单…… | D | 中文省略号应使用“……”而非半角省略号“...”。 |
| 6648 | You cannot join this session because it is full. | 该场次已满，无法加入。 | 该会话已满，无法加入。 | D | 根据已落地术语，多人联网语境下的 session 应译为“会话”，原译“场次”不准确。 |
| 6673 | OPEN NAT is the optimal setting. You will join sessions and communicate with other players without experiencing any prob | OPEN NAT 是最佳设置。你将加入即兴演奏并与其他玩家交流，且不会遇到任何问题。 | OPEN NAT 是最佳设置。你将加入会话并与其他玩家交流，且不会遇到任何问题。 | D | 根据语境例外，多人联网语境下的 session 应译为“会话”，而非“即兴演奏”。 |
| 6676 | OPEN NAT is the optimal setting. You will join sessions and communicate with other players without experiencing any prob | OPEN NAT 是最佳设置。你将加入即兴演奏并与其他玩家交流，且不会遇到任何问题。 | OPEN NAT 是最佳设置。你将加入会话并与其他玩家交流，且不会遇到任何问题。 | D | 原文 'join sessions' 指多人联网会话，非即兴演奏模式，需译为会话 |
| 6679 | OPEN NAT is the optimal setting. You will join sessions and communicate with other players without experiencing any prob | OPEN NAT 是最佳设置。你将加入即兴演奏并与其他玩家交流，且不会遇到任何问题。 | OPEN NAT 是最佳设置。你将加入会话并与其他玩家交流，且不会遇到任何问题。 | D | 根据术语表，多人联网语境下的 session 应译为“会话”，原译“即兴演奏”错误。 |
| 6681 | Your NAT type is MODERATE (NAT Type 2). You will not be able to play or communicate with players who have CLOSED NAT (NA | 您的 NAT 类型为中等（NAT 类型 2）。您将无法与 NAT 类型为封闭（NAT 类型 3）的玩家进行游戏或通信。 | 你的 NAT 类型为中等（NAT 类型 2）。你将无法与 NAT 类型为封闭（NAT 类型 3）的玩家进行游戏或通信。 | D | 玩家用你；原译使用“您”，违反代词规则。 |
| 6682 | Your NAT type is MODERATE (NAT Type 2). You will not be able to play or communicate with players who have CLOSED NAT (NA | 您的 NAT 类型为中等（NAT 类型 2）。您将无法与 NAT 类型为封闭（NAT 类型 3）的玩家进行游戏或通信。 | 你的 NAT 类型为中等（NAT 类型 2）。你将无法与 NAT 类型为封闭（NAT 类型 3）的玩家进行游戏或通信。 | D | 统一使用“你”作为玩家代词，避免“您”与“你”混用 |
| 6689 | Your NAT type is OPEN. OPEN NAT is the optimal setting. You will join games and communicate with other players without e | 您的 NAT 类型为 OPEN。OPEN NAT 是最佳设置。您可以顺利加入游戏并与其他玩家通信，不会遇到任何问题。 | 你的 NAT 类型为 OPEN。OPEN NAT 是最佳设置。你可以顺利加入游戏并与其他玩家通信，不会遇到任何问题。 | D | 模型未提供理由，需复核 |
| 6690 | Your NAT type is OPEN. OPEN NAT is the optimal setting. You will join games and communicate with other players without e | 您的 NAT 类型为 OPEN。OPEN NAT 是最佳设置。您可以顺利加入游戏并与其他玩家通信，不会遇到任何问题。 | 你的 NAT 类型为 OPEN。OPEN NAT 是最佳设置。你可以顺利加入游戏并与其他玩家通信，不会遇到任何问题。 | D | 统一使用“你”作为玩家代词，避免“您”与“你”混用 |
| 6691 | Your NAT type is OPEN. OPEN NAT is the optimal setting. You will join games and communicate with other players without e | 您的 NAT 类型为 OPEN。OPEN NAT 是最佳设置。您可以顺利加入游戏并与其他玩家通信，不会遇到任何问题。 | 你的 NAT 类型为 OPEN。OPEN NAT 是最佳设置。你可以顺利加入游戏并与其他玩家通信，不会遇到任何问题。 | D | 统一使用“你”作为玩家代词，原译“您”不符合规则5及本桶重点要求 |
| 6692 | Your NAT type is OPEN (NAT Type 1). OPEN NAT is the optimal setting. You will join games and communicate with other play | 你的 NAT 类型为开放型（NAT 类型 1）。开放型 NAT 是最佳设置。你将能够加入游戏并与其他玩家通信，且不会遇到任何问题。 | 你的 NAT 类型为开放（NAT 类型 1）。开放 NAT 是最佳设置。你将能够加入游戏并与其他玩家通信，且不会遇到任何问题。 | D | NAT 类型 OPEN 应译为“开放”以对应中文语境，原译“开放型”虽可接受但“开放”更简洁且符合技术术语习惯 |
| 6694 | Your NAT type is OPEN (NAT Type 1). OPEN NAT is the optimal setting. You will join games and communicate with other play | 你的 NAT 类型为开放型（NAT 类型 1）。开放型 NAT 是最佳设置。你将能够加入游戏并与其他玩家通信，且不会遇到任何问题。 | 你的 NAT 类型为开放（NAT 类型 1）。开放 NAT 是最佳设置。你将能够加入游戏并与其他玩家通信，且不会遇到任何问题。 | D | NAT 类型 OPEN 应译为“开放”以对应中文语境，原译“开放型”虽可接受但“开放”更简洁且符合技术术语习惯 |
| 6782 | The group leader has changed. | 群组领导者已变更。 | 队长已变更。 | D | 根据已落地术语，group leader 应译为“队长”，而非“群组领导者”。 |
| 6784 | You have been removed from the session by the group leader. | 你已被房主移出场次。 | 你已被队长移出会话。 | D | 原文 'group leader' 对应术语 '队长'，现译 '房主' 错误；原文 'session' 对应术语 '会话'，现译 '场次' 错误。 |
| 6785 | You have been removed from the session by the group leader. | 你已被房主移出场次。 | 你已被队长移出会话。 | D | source 中 group leader 对应术语“队长”，session 在多人语境下对应“会话”，原译“房主”和“场次”不符合既定术语规范。 |
| 6822 | The group leader has changed. | 群组领导者已变更。 | 队长已变更。 | D | 模型未提供理由，需复核 |
| 6823 | We are unable to determine your NAT Type. This may have an impact on the quality of the online experience. | 我们无法确定您的 NAT 类型。这可能会影响在线体验的质量。 | 我们无法确定你的 NAT 类型。这可能会影响在线体验的质量。 | D | 统一使用“你”作为玩家代词，原译“您”不符合规则5及本桶重点要求 |
| 6836 | The match you’re attempting to join is using game content you haven’t purchased or unlocked yet. Please visit the PlaySt | 你尝试加入的比赛使用了你尚未购买或解锁的游戏内容。请访问 PlayStation®Store 或 Uplay 商店获取该内容。 | 你尝试加入的对局使用了你尚未购买或解锁的游戏内容。请访问 PlayStation®Store 或 Uplay 商店获取该内容。 | D | 原文 'match' 对应术语 '对局'，现译 '比赛' 不符合游戏术语规范。 |
| 6837 | Game session no longer available because you've signed out of the PlayStation®Network. You'll return to the single playe | 由于您已退出 PlayStation®Network，该游戏会话不再可用。您将返回单人模式。 | 由于你已退出 PlayStation®Network，该游戏会话不再可用。你将返回单人模式。 | D | 统一使用“你”作为玩家代词，原译“您”不符合规则5及本桶重点要求 |
| 6838 | The match you’re attempting to join is using game content you haven’t purchased or unlocked yet. Please visit the PlaySt | 你尝试加入的比赛使用了你尚未购买或解锁的游戏内容。请访问 PlayStation®Store 或 Uplay 商店获取该内容。 | 你尝试加入的对局使用了你尚未购买或解锁的游戏内容。请访问 PlayStation®Store 或 Uplay 商店获取该内容。 | D | 根据已落地术语 match=对局，原译“比赛”错误，应改为“对局”。 |
| 6839 | The match you’re attempting to join is using game content you haven’t purchased or unlocked yet. Please visit the PlaySt | 你尝试加入的比赛使用了你尚未购买或解锁的游戏内容。请访问 PlayStation®Store 或 Uplay 商店获取该内容。 | 你尝试加入的对局使用了你尚未购买或解锁的游戏内容。请访问 PlayStation®Store 或 Uplay 商店获取该内容。 | D | 根据术语表，match 应译为“对局”，而非“比赛”。 |
| 6853 | Connection to host timed out. You will be returned to the title screen. | 连接主机超时。你将返回标题屏幕。 | 连接房主超时。你将返回标题屏幕。 | D | 在多人游戏语境中，host 指房主，原译“主机”易与硬件主机混淆 |
| 6899 | Awaiting response from the host… %d | 等待主机响应… %d | 等待房主响应… %d | D | 根据已落地术语，host 应译为“房主”，原译“主机”易与硬件设备混淆，且不符合多人游戏语境规范。 |
| 6903 | Connection to host timed out. You will be returned to the title screen. | 连接主机超时。你将返回标题屏幕。 | 连接房主超时。你将返回标题屏幕。 | D | 根据术语表，host 应译为“房主”，现译“主机”易与硬件设备混淆，且不符合多人模式角色术语规范。 |
| 6923 | You have been returned to the main menu because you signed out from the PlayStation®Network. | 由于你已从 PlayStation®Network 登出，你已被返回主菜单。 | 由于你已从 PlayStation®Network 登出，你已返回主菜单。 | D | 模型未提供理由，需复核 |
| 6925 | Awaiting response from the host… %d | 等待主机响应… %d | 等待房主响应… %d | D | 根据术语表，host 应译为“房主”，现译“主机”易与硬件设备混淆，且不符合多人模式角色术语规范。 |
| 6927 | Cannot join this match. The host is using content that you have not yet downloaded. Please visit the PlayStation®Store t | 无法加入此比赛。房主正在使用您尚未下载的内容。请访问 PlayStation®Store 下载额外的游戏内容。 | 无法加入此对局。房主正在使用你尚未下载的内容。请访问 PlayStation®Store 下载额外的游戏内容。 | D | 根据术语表，match 应译为“对局”；根据代词规则，玩家应用“你”而非“您”。 |
| 6929 | The connection to the host has been lost. | 与主机的连接已断开。 | 与房主的连接已断开。 | D | 原文 'host' 对应术语 '房主'，现译 '主机' 易与硬件设备混淆，应使用角色术语。 |
| 7092 | Game session no longer available because you've signed out of the PlayStation®Network. You'll return to the single playe | 由于您已退出 PlayStation®Network，该游戏会话不再可用。您将返回单人模式。 | 由于你已退出 PlayStation®Network，该游戏会话不再可用。你将返回单人模式。 | D | 根据代词规则，玩家应用“你”而非“您”。 |
| 7134 | Please point at the screen with the PlayStation®Move motion controller. If you are already doing it{C} hold the Move and | 请使用 PlayStation®Move 体感控制器指向屏幕。如果您已经在这样做{C} 请按住 Move 和 T 按钮几秒钟以校准 PlayStation®Move 体感控制器。 | 请使用 PlayStation®Move 动作控制器指向屏幕。如果你已经在这样做{C} 请按住 Move 和 T 按钮几秒钟以校准 PlayStation®Move 动作控制器。 | D | 统一 PlayStation®Move 的译名为“动作控制器”，并将“您”改为“你”以符合玩家称呼规范。 |
| 7181 | Online service is disabled on your Sony Entertainment Network account due to parental control restrictions. | 由于家长控制限制，您的 Sony Entertainment Network 账户已禁用在线服务。 | 由于家长控制限制，你的 Sony Entertainment Network 账户已禁用在线服务。 | D | 统一使用“你”作为玩家代词，避免“您”与“你”混用 |
| 7190 | You have been returned to the main menu because you signed out from the PlayStation®Network. | 由于你已从 PlayStation®Network 登出，你已被返回主菜单。 | 由于你已从 PlayStation®Network 登出，已返回主菜单。 | D | 原译“你已被返回主菜单”存在翻译腔，中文习惯省略被动主语，直接表述状态变化。 |
| 7196 | Awaiting response from the host… %d | 等待主机响应… %d | 等待房主响应… %d | D | 根据术语表，host 应译为“房主”，原译“主机”易与硬件设备混淆。 |
| 7198 | Cannot join this match. The host is using content that you have not yet downloaded. Please visit the PlayStation®Store t | 无法加入此比赛。房主正在使用您尚未下载的内容。请访问 PlayStation®Store 下载额外的游戏内容。 | 无法加入此对局。房主正在使用您尚未下载的内容。请访问 PlayStation®Store 下载额外的游戏内容。 | D | 根据术语表，match 应统一译为“对局”，现译“比赛”不符合 Rocksmith 多人模式术语规范。 |
| 7266 | Please point at the screen with the PlayStation®Move motion controller. If you are already doing it{C} hold the Move and | 请使用 PlayStation®Move 体感控制器指向屏幕。如果您已经在这样做{C} 请按住 Move 和 T 按钮几秒钟以校准 PlayStation®Move 体感控制器。 | 请使用 PlayStation®Move 体感控制器指向屏幕。如果你已经在这样做{C} 请按住 Move 和 T 按钮几秒钟以校准 PlayStation®Move 体感控制器。 | D | 根据规则，玩家应用“你”而非“您” |
| 7321 | The connection to the host has been lost.  This game will not count towards your ranking. | 与主机的连接已断开。本局游戏将不计入你的排名。 | 与房主的连接已断开。本局游戏将不计入你的排名。 | D | 根据已落地术语，host 应译为“房主”，而非“主机”。 |
| 7322 | The host has left the match. | 房主已离开比赛。 | 房主已离开对局。 | D | 根据术语表，match 应译为“对局”，而非“比赛”。 |
| 7323 | The host has left the match. | 房主已离开比赛。 | 房主已离开对局。 | D | 模型未提供理由，需复核 |
| 7337 | The connection to the host has been lost. | 与主机的连接已断开。 | 与房主的连接已断开。 | D | 根据术语表，host 应译为“房主”而非“主机” |
| 7348 | The connection to the host has been lost.  This game will not count towards your ranking. | 与主机的连接已断开。本局游戏将不计入你的排名。 | 与房主的连接已断开。本局游戏将不计入你的排名。 | D | 根据已落地术语，host 应译为“房主”而非“主机”，以避免与硬件主机混淆。 |
| 7359 | You cannot join this session because it is full. | 该场次已满，无法加入。 | 该会话已满，无法加入。 | D | 根据术语表，多人联网语境下的 session 应译为“会话”，原译“场次”不准确。 |
| 7365 | Could not join match{C} the game is full. | 无法加入比赛{C}游戏已满。 | 无法加入对局{C}游戏已满。 | D | 根据已落地术语 match=对局，原译“比赛”错误，应改为“对局”。 |
| 7373 | Cancelling quick match… | 正在取消快速匹配… | 正在取消快速匹配…… | D | 根据规则20，中文省略号应使用“……”而非“…”。 |
| 7444 | No games match your criteria. | 没有符合您条件的游戏。 | 没有符合你条件的游戏。 | D | 模型未提供理由，需复核 |
| 7458 | The match you've selected is currently in progress. You'll be in observer mode until the next round. Do you want to join | 你选择的比赛正在进行中。在下一轮开始前，你将处于观察者模式。要加入这场比赛吗？ | 你选择的对局正在进行中。在下一轮开始前，你将处于观察者模式。要加入这个对局吗？ | D | 根据术语表，match 应统一译为“对局”，原译“比赛”不符合规范 |
| 7461 | Unable to join the match. The connection is not responding. | 无法加入比赛。连接无响应。 | 无法加入对局。连接无响应。 | D | 根据已落地术语，match 应译为“对局”，而非“比赛”。 |
| 7464 | Unable to join the match. The connection is not responding. | 无法加入比赛。连接无响应。 | 无法加入对局。连接无响应。 | D | 根据术语表，match 应统一译为“对局”，现译“比赛”不符合 Rocksmith 多人模式术语规范。 |
| 7470 | Match no longer available. | 比赛已不可用。 | 对局已不可用。 | D | 根据已落地术语，match 应译为“对局”，原译“比赛”不准确 |
| 7471 | Match no longer available. | 比赛已不可用。 | 对局已不可用。 | D | 根据已落地术语，match 应译为“对局”，而非“比赛”。 |
| 7526 | Your connection to Xbox LIVE has been lost. You will be returned to the main menu. | 与 Xbox LIVE 的连接已断开。您将返回主菜单。 | 与 Xbox LIVE 的连接已断开。你将返回主菜单。 | D | 统一使用“你”作为玩家代词，避免“您”与“你”混用 |
| 7532 | You have been disconnected from the host. Returning to the Multiplayer menu. | 你已与主机断开连接。正在返回多人模式菜单。 | 你已与房主断开连接。正在返回多人模式菜单。 | D | 根据已落地术语，host 应译为“房主”而非“主机”，以准确指代多人会话中的房主角色。 |
| 7533 | You have been disconnected from the host. Returning to the Multiplayer menu. | 你已与主机断开连接。正在返回多人模式菜单。 | 你已与房主断开连接。正在返回多人模式菜单。 | D | 根据术语表，host 应译为“房主”而非“主机” |
| 7538 | Creating match... | 正在创建匹配... | 正在创建对局... | D | 根据已落地术语，match 应译为“对局”，此处“创建匹配”语义不准确，应为创建对局。 |
| 7539 | Cannot join this match at this time. Please try again later. | 当前无法加入此比赛。请稍后再试。 | 当前无法加入此对局。请稍后再试。 | D | 根据术语表，match 应统一译为“对局”，现译“比赛”不符合 Rocksmith 多人模式术语规范。 |
| 7540 | Cannot join this match at this time. Please try again later. | 当前无法加入此比赛。请稍后再试。 | 当前无法加入此对局。请稍后再试。 | D | 原文 'match' 对应术语 '对局'，现译 '比赛' 不符合游戏术语规范。 |
| 7541 | Creating match... | 正在创建匹配... | 正在创建对局…… | D | 根据已落地术语，match 应译为“对局”；中文省略号应使用“……”。 |
| 7543 | Joining match... | 正在加入比赛... | 正在加入对局... | D | 根据术语表，match 应译为“对局”，而非“比赛”。 |
| 7544 | Leaving the match… | 正在退出比赛…… | 正在退出对局…… | D | 根据已落地术语，match 应统一译为“对局”而非“比赛”。 |
| 7545 | Leaving the match… | 正在退出比赛…… | 正在退出对局…… | D | 模型未提供理由，需复核 |
| 7546 | Joining match... | 正在加入比赛... | 正在加入对局... | D | match 统一译为对局；原译“比赛”不符合已落地术语。 |
| 7547 | Could not join match{C} the game is full. | 无法加入比赛{C}游戏已满。 | 无法加入对局{C}游戏已满。 | D | 根据术语表，match 应译为“对局”，现译“比赛”不准确 |
| 7591 | ranked match | 排位赛 | 排位对局 | D | 根据已落地术语，match 应译为“对局”，而非“赛”。 |
| 7641 | custom match | 自定义比赛 | 自定义对局 | D | match 统一译为对局；原译“比赛”不符合已落地术语。 |
| 7642 | custom match | 自定义比赛 | 自定义对局 | D | 根据术语表，match 应译为“对局”，原译“比赛”不符合游戏语境。 |
| 7643 | custom match | 自定义比赛 | 自定义对局 | D | 根据已落地术语规则，match 应译为“对局”而非“比赛” |
| 7667 | player match | 玩家匹配 | 玩家对局 | D | 根据已落地术语 match=对局，原译“匹配”错误，应改为“对局”。 |
| 7779 | Xbox LIVE Player Match | Xbox LIVE 玩家匹配 | Xbox LIVE 玩家对局 | D | 模型未提供理由，需复核 |
| 7781 | Private Match | 私人对战 | 私人对局 | D | match 统一译为对局；原译“对战”不符合已落地术语。 |
| 21243 | You are currently not signed in. If you continue{C} you will not be able to save your game or use any feature that requi | 你当前未登录。如果你继续{C} 将无法保存游戏或使用任何需要玩家资料的功能。 | 你当前未登录。如果你继续{C} 将无法保存游戏或使用任何需要玩家档案的功能。 | D | 根据已落地术语，profile 应译为“玩家档案”而非“玩家资料”。 |
| 22210 | Ideal for letting a new player play a song without changing profiles{C} this setting allows you to easily reset all song | 适合让新玩家在不切换配置文件的情况下演奏歌曲{C} 此设置允许你将所有歌曲轻松重置为最低难度。之后{C} 你可以将所有歌曲恢复到你达到的最高难度。 | 适合让新玩家在不切换玩家档案的情况下演奏歌曲{C} 此设置允许你将所有歌曲轻松重置为最低难度。之后{C} 你可以将所有歌曲恢复到你达到的最高难度。 | D | 根据已落地术语规则，profile 应译为“玩家档案”而非“配置文件” |
| 22845 | Your save data will now be updated. Uninstalling the latest patch will cause your save data to be incompatible with prev | 您的存档数据现在将更新。卸载最新补丁会导致存档数据与 Rocksmith 的旧版本不兼容。如果补丁丢失{C}请登录 PlayStation®Network 并下载最新补丁。 | 你的存档数据现在将更新。卸载最新补丁会导致存档数据与 Rocksmith 的旧版本不兼容。如果补丁丢失{C}请登录 PlayStation®Network 并下载最新补丁。 | D | 统一使用“你”作为玩家代词，原译“您”不符合规则5及本桶重点要求 |
| 23426 | Change profiles? | 更改配置文件？ | 更改玩家档案？ | D | 根据已落地术语，profile 应译为“玩家档案”而非“配置文件”。 |
| 23427 | Do you want to switch profiles? | 要切换配置文件吗？ | 要切换玩家档案吗？ | D | 根据已落地术语，profile 应译为“玩家档案”，原译“配置文件”不符合术语规范。 |
| 25121 | It's always dramatic when someone slides all the way up the neck to play a screaming solo on the higher frets. There is  | 当有人滑到琴颈高处演奏高把位尖叫独奏时，场面总是很震撼。有一个酷炫的技巧能让你比想象中更快到达那里。{L}{L}每个音阶形状在琴颈高12品处都有一个完全相同的复制品。那个位置高一个八度。快速跳转12品的简单方法是假装双点后的第一个点是3{C | 当有人滑到琴颈高处演奏高把位尖叫独奏时，场面总是很震撼。有一个酷炫的技巧能让你比想象中更快到达那里。{L}{L}每个音阶指型在琴颈高12品处都有一个完全相同的复制品。那个位置高一个八度音程。快速跳转12品的简单方法是假装双点后的第一个点是3 | D | 根据术语表，Scale Shape 应译为“音阶指型”，Octave 在音程任务中应保留“八度音程” |

### 桶 E（152）

| id | source | original | revised | 分类 | reason |
|---|---|---|---|---|---|
| 6892 | directional pad | 方向键 | 十字键 | E | D-pad 统一译为“十字键”，而非“方向键”。 |
| 10480 | Another popular option is amp modeling{C} where the characteristic sound of an amplifier is emulated digitally. You can  | 另一个流行选项是音箱建模{C}即通过数字方式模拟音箱的特征音色。你可以在独立组合音箱或计算机软件中找到音箱建模功能。这是一种从单个音箱中获取多种截然不同音色的绝佳方式。 | 另一个流行选项是音箱建模{C}即通过数字方式模拟音箱的特征音色。你可以在独立一体式音箱或计算机软件中找到音箱建模功能。这是一种从单个音箱中获取多种截然不同音色的绝佳方式。 | E | combo 已落地术语为“一体式音箱”，原译“组合音箱”错误。 |
| 12437 | You can get amps where that part that amplifies the signal - that's called the head - is separate from the speaker cabin | 你可以购买将放大信号的部件（称为头）与音箱箱体分离的音箱{C}或者购买一体式音箱{C}即组合音箱。组合音箱通常更便携，对初学者来说可能是更好的起点。 | 你可以购买将放大信号的部件（称为音箱头）与箱体分离的音箱{C}或者购买一体式音箱{C}即组合音箱。组合音箱通常更便携，对初学者来说可能是更好的起点。 | E | 原文 'head' 指音箱头，'speaker cabinet' 指箱体，现译将 head 误译为“头”，cabinet 误译为“音箱箱体”，违反设备结构专用词义规则。 |
| 17414 | To equip a guitar with a different headstock{C} go to the Amp and choose to customize your guitar. | 要为吉他更换不同的琴头{C} 请前往 Amp 并选择自定义您的吉他。 | 要为吉他更换不同的琴头{C} 请前往 Amp 并选择自定义你的吉他。 | E | 模型未提供理由，需复核 |
| 17609 | Unlocked Effects Pedal | 已解锁效果器 | 已解锁效果器踏板 | E | 规则14：同一控件或功能名在标题、任务和说明中使用同一译名；source 为 Effects Pedal，现译漏译 Pedal，且其他条目（如 21877）均译为“效果器踏板”。 |
| 17690 | Combo Event | 连击事件 | 连击活动 | E | 根据已落地术语，event(活动)应译为活动，而非事件。 |
| 17781 | Authentic Tone Reward | 真实音色奖励 | 原曲音色奖励 | E | Authentic Tone 已落地术语为“原曲音色” |
| 17808 | Unlock the Tone Slots by unlocking an Authentic Tone for any arrangement. | 通过为任意编曲解锁真实音色来解锁音色槽位。 | 通过为任意编曲解锁原曲音色来解锁音色槽位。 | E | 根据已落地术语，Authentic Tone 应统一译为“原曲音色”，现译“真实音色”不符合术语规范。 |
| 17824 | Now you're ready to graduate from the basic tone and play like a true guitarist{C} with the songs' authentic tones. | 现在你准备好从基础音色毕业，像真正的吉他手一样{C}使用歌曲的原声音色进行演奏。 | 现在你准备好从基础音色毕业，像真正的吉他手一样{C}使用歌曲的原曲音色进行演奏。 | E | 根据已落地术语，Authentic Tone 应统一译为“原曲音色”，现译“原声音色”不准确。 |
| 17826 | To learn more about authentic and custom tones{C} watch the tone creation walkthrough video. | 要了解关于真实音色和自定义音色的更多信息{C}请观看音色创建教程视频。 | 要了解关于原曲音色和自定义音色的更多信息{C}请观看音色创建教程视频。 | E | 规则14：Authentic Tone 统一译为原曲音色。 |
| 17839 | Press the A button to use the song's authentic tone. | 按下 A 按钮以使用歌曲的原生音色。 | 按下 A 按钮以使用歌曲的原曲音色。 | E | authentic tone 已落地术语为“原曲音色”，原译“原生音色”错误。 |
| 17840 | Press the cross button to use the song's authentic tone. | 按十字键使用歌曲的原版音色。 | 按叉键使用歌曲的原曲音色。 | E | cross button 应译为叉键，authentic tone 应译为原曲音色 |
| 17841 | Press the X button to use the song's authentic tone. | 按 X 键使用歌曲的原版音色。 | 按 X 键使用歌曲的原曲音色。 | E | 根据规则14，Authentic Tone 统一译为“原曲音色”，现译“原版音色”不准确。 |
| 17850 | To scroll fast through songs{C} hold down the d-pad in the direction you'd like to scroll. | 若要快速滚动歌曲列表{C}按住方向键朝你想滚动的方向即可。 | 若要快速滚动歌曲列表{C}按住十字键朝你想滚动的方向即可。 | E | D-pad 应译为十字键，而非方向键 |
| 18335 | Head [1] | 琴头 [1] | 音箱头 [1] | E | 在设备/效果器语境下，head 指“音箱头”，而非吉他琴头。 |
| 19305 | This product includes the song [SongName] by [ArtistName]{C} [X] playable arrangements (Arrangement Names){C} and an unl | 本产品包含 [ArtistName] 的歌曲 [SongName]{C} [X] 个可玩编曲（编曲名称）{C} 以及一个可解锁的真实音色。 | 本产品包含 [ArtistName] 的歌曲 [SongName]{C} [X] 个可玩编曲（编曲名称）{C} 以及一个可解锁的原曲音色。 | E | 模型未提供理由，需复核 |
| 19306 | Authentic Tone includes the customization items: [Item Names] | 真实音色包含以下自定义项目：[Item Names] | 原曲音色包含以下自定义项目：[Item Names] | E | 模型未提供理由，需复核 |
| 19307 | This product includes the song “[1]” by [2]{C} [3] playable arrangements{S} and an unlockable Authentic Tone. | 此产品包含歌曲“[1]”由 [2]{C} [3] 可玩编曲{S} 以及可解锁的真实音色。 | 此产品包含歌曲“[1]”由 [2]{C} [3] 可玩编曲{S} 以及可解锁的原曲音色。 | E | 模型未提供理由，需复核 |
| 20427 | Default to Authentic Tone | 默认使用真实音色 | 默认使用原曲音色 | E | Authentic Tone 已落地术语为“原曲音色”，原译“真实音色”错误。 |
| 20465 | Turn the noise canceling tone off and enable Authentic Song Tones. | 关闭降噪音色并启用真实歌曲音色。 | 关闭降噪音色并启用原曲音色。 | E | 已落地术语规定 Authentic Tone 应译为“原曲音色”，现译“真实歌曲音色”不符合术语规范。 |
| 20982 | Play with the percieved size of your sound with this sample delay pedal. | 使用这个采样延迟效果器来改变你声音的感知大小。 | 使用这款采样延迟效果器来改变你声音的感知大小。 | E | 模型未提供理由，需复核 |
| 20986 | The I-505 is a vintage drive pedal with mods especially for the modern musician. | I-505 是一款经过改装的复古失真效果器，专为现代音乐家设计。 | I-505 是一款经过改装的复古过载效果器，专为现代音乐家设计。 | E | 原文 drive pedal 在规则12中明确不译驱动，且区别于 fuzz，应译为过载效果器 |
| 21073 | Load Authentic Tone | 加载真实音色 | 加载原曲音色 | E | 已落地术语规定 Authentic Tone 统一译为“原曲音色” |
| 21084 | Change Cabinet | 更换机柜 | 更换箱体 | E | 根据规则11，cabinet在吉他设备语境下应译为“箱体” |
| 21092 | [1] Cabinet | [1] 机柜 | [1] 箱体 | E | Cabinet 在吉他设备语境下应译为箱体 |
| 21112 | Change Cabinet | 更换机柜 | 更换箱体 | E | 根据已落地术语，cabinet 在音箱语境下应译为“箱体”，而非“机柜” |
| 21133 | Delete the currently loaded Custom Tone.{L}NOTE: Authentic Tones cannot be deleted. | 删除当前加载的自定义音色。{L}注意：真实音色无法删除。 | 删除当前加载的自定义音色。{L}注意：原曲音色无法删除。 | E | Authentic Tones 应译为“原曲音色” |
| 21134 | This tone name belongs to an Authentic Tone and cannot be overwritten. Please choose a new name. | 此音色名称属于真实音色，无法覆盖。请选择新名称。 | 此音色名称属于原曲音色，无法覆盖。请选择新名称。 | E | Authentic Tone 已落地术语为“原曲音色”，原译“真实音色”错误。 |
| 21137 | Unlock this Authentic Tone by scoring 70{C}000 the following song: | 在以下歌曲中得分达到 70{C}000 即可解锁此真实音色： | 在以下歌曲中得分达到 70{C}000 即可解锁此原曲音色： | E | Authentic Tone 应译为原曲音色 |
| 21149 | To scroll fast through the Tracker{C} hold down the d-pad in the direction you'd like to scroll. | 要快速滚动 Tracker{C}请按住方向键朝你想滚动的方向。 | 要快速滚动 Tracker{C}请按住十字键朝你想滚动的方向。 | E | D-pad 应译为十字键，原译“方向键”不准确 |
| 21643 | New Cabinet Unlocked | 已解锁新音箱箱体 | 已解锁新箱体 | E | 模型未提供理由，需复核 |
| 21846 | Create and save a custom tone | 的自定义音色方案 | 创建并保存自定义音色 | E | 规则18：识别整句漏译；source 为动词短语 Create and save...，现译“的自定义音色方案”缺失动词且语法不通，应为“创建并保存自定义音色”。 |
| 21934 | The Rocksmith Custom Drive | Rocksmith 定制驱动 | Rocksmith 定制过载 | E | 规则12：overdrive 语境的 drive 不译驱动，应译为过载。 |
| 22009 | Authentic Song Tone | 真实歌曲音色 | 原曲音色 | E | 根据已落地术语，Authentic Tone 统一译为“原曲音色”，现译“真实歌曲音色”不符合术语规范。 |
| 22044 | Authentic Tone | 真实音色 | 原曲音色 | E | 根据已落地术语，Authentic Tone 应译为“原曲音色”，现译“真实音色”不符合术语规范。 |
| 22461 | Modern Ultra- HiFi Bass Cab | 现代超高保真贝斯音箱 | 现代超高保真贝斯箱体 | E | 模型未提供理由，需复核 |
| 22467 | Modular Open/Closed Back Cab | 模块化开背/闭背音箱 | 模块化开背/闭背箱体 | E | 模型未提供理由，需复核 |
| 22559 | Bass Head | Bass Head | 贝斯音箱头 | E | head 指音箱头，Bass Head 即贝斯音箱头 |
| 22838 | Tip: Press F1 to return your tone back to the song's authentic tone … | 提示：按 F1 可将音色恢复为歌曲的原声音色…… | 提示：按 F1 可将音色恢复为歌曲的原曲音色…… | E | Authentic Tone 已落地术语为“原曲音色” |
| 22840 | Press F4 to return your tone back to the song's authentic tone. | 按 F4 将音色恢复为歌曲的原生音色。 | 按 F4 将音色恢复为歌曲的原曲音色。 | E | 根据已落地术语，authentic tone 应统一译为“原曲音色”，而非“原生音色”。 |
| 22885 | Every song in Rocksmith features an authentic tone capturing the distinctive sounds of your favorite bands. | Rocksmith 中的每首歌都具备真实音色，捕捉你喜爱乐队的独特声音。 | Rocksmith 中的每首歌都具备原曲音色，捕捉你喜爱乐队的独特声音。 | E | 根据已落地术语，Authentic Tone 应统一译为“原曲音色”，现译“真实音色”不准确。 |
| 25014 | Now let's try playing with a really popular scale{C} the Pentatonic Minor. This scale is a breeding ground for tons of R | 现在让我们尝试演奏一个非常流行的音阶{C}五声音阶小调。这个音阶是大量摇滚和布鲁斯乐句的源泉{C}而且它的箱型指法非常独特。许多乐队仅靠在这个音阶上即兴演奏就建立了职业生涯。 | 现在让我们尝试演奏一个非常流行的音阶{C}五声音阶小调。这个音阶是大量摇滚和布鲁斯乐句的源泉{C}而且它的音阶指型非常独特。许多乐队仅靠在这个音阶上即兴演奏就建立了职业生涯。 | E | 原文 box shape 在吉他教学语境中指音阶指型（Scale Shape），现译“箱型指法”不符合已落地术语规范。 |
| 26046 | All the songs in Rocksmith have Authentic Tones. Let's load up a tone from a song you like. | Rocksmith 中的所有歌曲都拥有真实音色。让我们加载一首你喜欢的歌曲的音色。 | Rocksmith 中的所有歌曲都拥有原曲音色。让我们加载一首你喜欢的歌曲的音色。 | E | 规则14：Authentic Tone 统一译为原曲音色。 |
| 26048 | While in AutoPilot{C} Rocksmith will always choose the Authentic Tone for what you are playing{C} BUT you can switch to  | 在自动演奏模式下{C}Rocksmith 总是为你演奏的内容选择真实音色{C}但你随时可以使用音色条切换到任何音色。现在让我们给音色条分配一个音色。 | 在自动演奏模式下{C}Rocksmith 总是为你演奏的内容选择原曲音色{C}但你随时可以使用音色条切换到任何音色。现在让我们给音色条分配一个音色。 | E | 根据已落地术语，Authentic Tone 应统一译为“原曲音色”，现译“真实音色”不符合术语规范。 |
| 26054 | When you're done creating a tone{C} Rocksmith auto-balances the volume of that tone{C} so all your custom and authentic  | 当你完成音色创建后{C}Rocksmith 会自动平衡该音色的音量{C}使所有自定义和真实音色的音量大致相同。我们强烈建议使用自动平衡{C}但你可以尝试手动平衡你的吉他音色。 | 当你完成音色创建后{C}Rocksmith 会自动平衡该音色的音量{C}使所有自定义和原曲音色的音量大致相同。我们强烈建议使用自动平衡{C}但你可以尝试手动平衡你的吉他音色。 | E | Authentic Tone 应译为原曲音色 |
| 26486 | While in Auto{C} Rocksmith will always choose the Authentic Tone for what you are playing{C} BUT you can switch to any T | 在自动模式下{C}Rocksmith 总是为你演奏的内容选择真实音色{C}但你随时可以使用音色条切换到任何音色。让我们现在为音色条分配一个音色。 | 在自动模式下{C}Rocksmith 总是为你演奏的内容选择原曲音色{C}但你随时可以使用音色条切换到任何音色。让我们现在为音色条分配一个音色。 | E | 已落地术语 Authentic Tone 必须译为原曲音色，现译真实音色错误 |
| 27187 | Overdriven Sine Pad | 过载正弦垫音 | 过载正弦铺底音色 | E | 规则11：音色语境的 pad 指铺底音色，不是实体垫子；原译“垫音”易误解为物理对象或错误术语。 |
| 27189 | Hexagon Pad | 六边形垫 | 六边形铺底音色 | E | 规则11：音色语境的 pad 指铺底音色，不是实体垫子。 |
| 27190 | Tremolo Pad | 颤音垫 | 颤音铺底音色 | E | 根据规则11，音色语境的 pad 指铺底音色，不应译为“垫”。 |
| 27463 | SESSION DRUMS | SESSION DRUMS | 即兴鼓组 | E | 已落地术语 Session Drums 必须译为即兴鼓组，现译保留英文错误 |
| 27510 | OVERDRIVEN SINE PAD | 过载正弦波垫音 | 过载正弦波铺底音色 | E | 根据规则11，音色语境的 pad 指铺底音色，不应译为“垫音”。 |
| 27657 | Create a custom tone plan with all unique{C} custom-created tones | 创建包含所有独特{C}自定义音色 | 创建包含所有独特{C}自定义音色的自定义音色方案 | E | 原文 'Create a custom tone plan' 意为创建自定义音色方案，现译漏译了 'plan'（方案/计划），导致句子结构不完整且语义缺失。 |
| 28852 | PROGRESSIVE PAD | 渐进式音垫 | 渐进式铺底音色 | E | 规则11指出音色语境的 pad 指铺底音色，不是踏板或实体垫子，原译“音垫”不符合专用词义。 |
| 28972 | SKY PAD | 天空垫 | 天空铺底音色 | E | 根据规则11，音色语境的 pad 指铺底音色，不应译为“垫”。 |
| 28974 | OVERDRIVEN SINE PAD | 过载正弦波垫音 | 过载正弦波铺底音色 | E | 根据规则11，音色语境的 pad 指铺底音色，现译“垫音”不准确。 |
| 28976 | HEXAGON PAD | 六边形垫 | 六边形铺底音色 | E | 规则11：音色语境的 pad 指铺底音色，不是实体垫子；原译“垫”易误解为物理对象。 |
| 30353 | A Cali custom shop '70s-style amp. | 一款 Cali 定制车间 70 年代风格 amp。 | 一款 Cali 定制车间 70 年代风格音箱。 | E | amp 应译为音箱，而非保留英文 |
| 30364 | A high-watt solid state amp. | 高瓦数电子管音箱。 | 高瓦数晶体管音箱。 | E | solid state 指晶体管/固态电路，非电子管（tube/vacuum tube） |
| 30390 | A US-style classic combo. | 一款美式经典组合音箱。 | 一款美式经典一体式音箱。 | E | 模型未提供理由，需复核 |
| 30394 | A 1935 vintage combo model with a10-watt amp. | 一款 1935 年的复古组合型号，配备 10 瓦音箱。 | 一款 1935 年的复古一体式音箱型号，配备 10 瓦音箱。 | E | combo 应译为“一体式音箱”而非“组合型号” |
| 30396 | A circa 1936 vintage combo model with a15-watt amp. | 一款约 1936 年的复古一体式型号，配备 15 瓦音箱。 | 一款约 1936 年的复古一体式音箱，配备 15 瓦音箱头。 | E | source 中 'amp' 在 'combo model' 语境下指内置的放大电路/音箱头，且 '15-watt amp' 通常指功率放大器部分，译为'音箱头'或保留'放大器'更准确，但根据已落地术语 amp=音箱，此处 'combo' 是一体式音箱，内部包含 amp。然而 '15-watt am |
| 30400 | A 1955 Epiphone® high-power combo with a 30-watt amp. | 一款 1955 年 Epiphone® 高功率组合音箱，配备 30 瓦 amp。 | 一款 1955 年 Epiphone® 高功率一体式音箱，配备 30 瓦音箱。 | E | combo 应译为一体式音箱，amp 应译为音箱 |
| 30418 | A very unique solid state amp built by Orange. | Orange 制造的非常独特的电子管音箱。 | Orange 制造的非常独特的晶体管音箱。 | E | 原文 solid state 指晶体管/固态电路，现译“电子管”与 tube 混淆，属技术错误。 |
| 30447 | A boutique transistor bass head. | 一款精品晶体管贝斯头。 | 一款精品晶体管贝斯音箱头。 | E | head 在设备语境下应译为“音箱头”，原译“贝斯头”错误。 |
| 30451 | A classic transistor bass head with tone-shaping EQ. | 一款带有音色塑形均衡的经典晶体管贝斯头。 | 一款带有音色塑形均衡的经典晶体管贝斯音箱头。 | E | 模型未提供理由，需复核 |
| 30455 | A classic tube bass head with deep drive and plenty of bite. | 一款经典电子管贝斯头，驱动深沉，咬劲十足。 | 一款经典电子管贝斯音箱头，驱动深沉，咬劲十足。 | E | 模型未提供理由，需复核 |
| 30457 | A boutique tube bass head with plenty of drive. | 一款驱动感十足的精品电子管贝斯头。 | 一款驱动感十足的精品电子管贝斯音箱头。 | E | 根据已落地术语，head 应译为“音箱头”，原译“贝斯头”不符合设备结构专用词义。 |
| 30463 | A classic Orange bass head with lots of gain and deep tone. | 一款经典 Orange 贝斯头，增益丰富，音色深沉。 | 一款经典 Orange 贝斯音箱头，增益丰富，音色深沉。 | E | 根据已落地术语，head 应译为音箱头，而非贝斯头。 |
| 30525 | Adds a classic flanger effect for jet-plane swooshes and fast liquid modulation. | 添加经典颤音效果，产生喷气式飞机呼啸声和快速液体调制效果。 | 添加经典镶边效果，产生喷气式飞机呼啸声和快速液体调制效果。 | E | Flanger 应译为“镶边效果”，与 ID 30526 保持一致 |
| 30526 | Modern Flanger | 现代颤音 | 现代镶边效果 | E | Flanger 在效果器语境下标准译名为“镶边效果”，“颤音”通常指 Vibrato 或 Tremolo |
| 30537 | A special fuzz pedal with extended tone control and tons of fuzz. | 带有扩展音色控制和大量失真音色的特殊法兹效果器。 | 带有扩展音色控制和大量法兹音色的特殊法兹效果器。 | E | 原文 tons of fuzz 指大量的法兹音色/效果，而非失真音色，且 fuzz 应译为法兹。 |
| 30658 | Orange OBC115 Bass Cab | Orange OBC115 贝斯音箱 | Orange OBC115 贝斯箱体 | E | 根据已落地术语，cab 应译为箱体，而非音箱。 |
| 30661 | A classic Orange 8x10 bass cab. | 一款经典 Orange 8x10 贝斯音箱。 | 一款经典 Orange 8x10 贝斯箱体。 | E | 模型未提供理由，需复核 |
| 30663 | A classic 8x10 bass cab. | 一款经典8x10贝斯音箱。 | 一款经典8x10贝斯箱体。 | E | cab 应译为箱体，而非音箱（amp） |
| 30665 | A classic closed-back 1x15 bass cab. | 一款经典封闭式1x15贝斯音箱。 | 一款经典封闭式1x15贝斯箱体。 | E | cab 应译为箱体 |
| 30673 | A unique multi-speaker bass cab. | 一款独特的多扬声器贝斯音箱。 | 一款独特的多扬声器贝斯箱体。 | E | 已落地术语规定 cab 应译为“箱体”，现译“音箱”不准确。 |
| 30675 | A classic ported 2x10 cab. | 一款经典倒相式 2x10 音箱。 | 一款经典倒相式 2x10 箱体。 | E | cab 应译为箱体，而非音箱（amp） |
| 30679 | A unique 3x12 folded bass cab. | 独特的 3x12 折叠式贝斯音箱。 | 独特的 3x12 折叠式贝斯箱体。 | E | 模型未提供理由，需复核 |
| 30683 | A custom 1x12 bass cab. | 一款定制 1x12 贝斯音箱。 | 一款定制 1x12 贝斯箱体。 | E | 模型未提供理由，需复核 |
| 30685 | A vintage 4x15 bass cab. | 复古 4x15 贝斯音箱。 | 复古 4x15 贝斯箱体。 | E | 模型未提供理由，需复核 |
| 30689 | An 8-inch open-back combo. | 一款8英寸开放式背板组合音箱。 | 一款 8 英寸开放式背板一体式音箱。 | E | combo 应译为“一体式音箱”，而非“组合音箱”。 |
| 30691 | A 10-inch open-back combo. | 一款 10 英寸开放式背板组合音箱。 | 一款 10 英寸开放式背板一体式音箱。 | E | combo 应译为“一体式音箱”，而非“组合音箱”。 |
| 30693 | A 12-inch closed-back combo. | 一款 12 英寸封闭式箱体组合音箱。 | 一款 12 英寸封闭式一体式音箱。 | E | combo 应译为'一体式音箱'，原译'箱体组合音箱'不符合已落地术语 combo=一体式音箱。 |
| 30698 | GA-88S Tweed Cab | GA-88S Tweed Cab | GA-88S Tweed 箱体 | E | source 中 Cab 指箱体，根据规则11 cab=箱体，不应保留英文 Cab 或译为音箱。 |
| 30700 | GA-8 Discoverer Cab | GA-8 Discoverer Cab | GA-8 Discoverer 箱体 | E | 模型未提供理由，需复核 |
| 30702 | Orange PPC412 Cab | Orange PPC412 音箱 | Orange PPC412 箱体 | E | 根据规则11，cab 应译为箱体，而非音箱。 |
| 30703 | A classic Orange 4x12 cab. | 一款经典 Orange 4x12 音箱。 | 一款经典 Orange 4x12 箱体。 | E | cab 应译为箱体，而非音箱（amp） |
| 30710 | A vintage Marshall 4x12 cab. | 一款复古Marshall 4x12音箱柜。 | 一款复古 Marshall 4x12 箱体。 | E | 模型未提供理由，需复核 |
| 30712 | A Marshall 4x12 extension cab. | Marshall 4x12 扩展音箱。 | Marshall 4x12 扩展箱体。 | E | 模型未提供理由，需复核 |
| 30725 | A Cali-style 2x15 cab. | 一款加州风格的 2x15 音箱。 | 一款加州风格的 2x15 箱体。 | E | 模型未提供理由，需复核 |
| 30729 | A classic Jazz 2x12. | 一款经典 Jazz 2x12 音箱。 | 一款经典 Jazz 2x12 箱体。 | E | 模型未提供理由，需复核 |
| 30733 | A rare vintage 2x15 cab. | 一款稀有的复古2x15音箱。 | 一款稀有的复古2x15箱体。 | E | cab 应译为箱体 |
| 30739 | A vintage UK-style 4x12. | 一款复古英式4x12音箱。 | 一款复古英式4x12箱体。 | E | 模型未提供理由，需复核 |
| 30763 | A boutique closed-back 1x12 cab. | 一款精品封闭式背板 1x12 音箱。 | 一款精品封闭式 1x12 箱体。 | E | cab 应译为箱体；closed-back 译为封闭式即可，无需加背板 |
| 30765 | A boutique open-back 1x12 cab. | 一款精品开放式背板 1x12 音箱。 | 一款精品开放式背板 1x12 箱体。 | E | 模型未提供理由，需复核 |
| 30998 | Vintage Flanger | 复古相位 | 复古颤音 | E | 规则12：效果器名称按功能翻译；Flanger 通常译为“颤音”或“镶边”，现译“相位”通常对应 Phaser，属于术语混淆。 |
| 31018 | Custom Drive | 自定义失真 | 自定义过载 | E | Drive 在效果器语境下通常译为过载 |
| 31128 | Orange OBC115 Bass Cab | Orange OBC115 贝斯音箱 | Orange OBC115 贝斯箱体 | E | 根据规则11，cab 应译为箱体，而非音箱。 |
| 31168 | GA-88S Tweed Cab | GA-88S Tweed Cab | GA-88S Tweed 箱体 | E | Cab 应译为箱体，Tweed 是材质/风格名保留英文 |
| 31257 | A high-watt solid state amp. | 高瓦数电子管音箱。 | 高瓦数晶体管音箱。 | E | solid state amp 指晶体管（固态）音箱，原译“电子管音箱”错误，电子管应为 tube/vacuum tube。 |
| 31283 | A US-style classic combo. | 一款美式经典组合音箱。 | 一款美式经典一体式音箱。 | E | combo 应译为一体式音箱 |
| 31287 | A 1935 vintage combo model with a10-watt amp. | 一款 1935 年的复古组合型号，配备 10 瓦音箱。 | 一款 1935 年的复古一体式音箱，配备 10 瓦音箱头。 | E | 模型未提供理由，需复核 |
| 31299 | A 1962 classic 15-watt combo. | 一款 1962 年经典的 15 瓦组合音箱。 | 一款 1962 年经典的 15 瓦一体式音箱。 | E | combo 应译为一体式音箱，而非组合音箱 |
| 31311 | A very unique solid state amp built by Orange. | Orange 制造的非常独特的电子管音箱。 | Orange 制造的非常独特的晶体管音箱。 | E | solid state 指晶体管/固态，非电子管。 |
| 31317 | Vintage Marshall drive with plenty of low-end. | 带有丰富低频的复古 Marshall 失真音色。 | 带有丰富低频的复古 Marshall 过载音色。 | E | drive 在效果器语境下通常译为过载，而非失真 |
| 31327 | A boutique tube/transistor hybrid bass amp with compression. | 一款带压缩的精品电子管/晶体管混合贝斯音箱。 | 一款带压缩的精品电子管/晶体管混合贝斯一体式音箱。 | E | 规则11：combo 应译为一体式音箱，而非音箱。 |
| 31339 | A boutique transistor bass head. | 一款精品晶体管贝斯头。 | 一款精品晶体管贝斯音箱头。 | E | head 在设备语境下应译为“音箱头”，原译“贝斯头”易产生歧义且不符合术语规范 |
| 31343 | A classic transistor bass head with tone-shaping EQ. | 一款带有音色塑形均衡的经典晶体管贝斯头。 | 一款带有音色塑形均衡的经典晶体管贝斯音箱头。 | E | 根据规则11，head 译为“音箱头”，现译“贝斯头”不准确。 |
| 31349 | A boutique tube bass head with plenty of drive. | 一款驱动感十足的精品电子管贝斯头。 | 一款驱动感十足的精品电子管贝斯音箱头。 | E | 根据规则11，head在设备结构中应译为“音箱头”，原译“贝斯头”易产生歧义且不符合术语规范。 |
| 31353 | A vintage tube bass head with bright character. | 一款音色明亮复古的电子管贝斯箱头。 | 一款音色明亮的复古电子管贝斯音箱头。 | E | head 在设备语境下应译为“音箱头”，原译“箱头”不符合已落地术语规范。 |
| 31355 | A classic Orange bass head with lots of gain and deep tone. | 一款经典 Orange 贝斯头，增益丰富，音色深沉。 | 一款经典 Orange 贝斯音箱头，增益丰富，音色深沉。 | E | 根据规则11及已落地术语，head 指人体头部时不译音箱头，此处为设备语境，应译为“音箱头”而非“贝斯头”。 |
| 31419 | Adds a modern flanger with extra controls. | 添加带有额外控制功能的现代颤音效果。 | 添加带有额外控制功能的现代镶边效果。 | E | flanger 应译为“镶边效果”，原译“颤音效果”混淆了 flanger 与 vibrato/tremolo 的功能区别。 |
| 31427 | A highly crunchy nasty fuzz pedal. | 一款音色粗粝刺耳的失真效果器。 | 一款音色粗粝刺耳的模糊效果器。 | E | 原文 fuzz pedal 在规则12中明确不译模糊，现译失真效果器错误 |
| 31555 | A classic 8x10 bass cab. | 一款经典8x10贝斯音箱。 | 一款经典8x10贝斯箱体。 | E | 模型未提供理由，需复核 |
| 31559 | A boutique ported 1x15 bass cab. | 一款精品倒相式1x15贝斯音箱。 | 一款精品倒相式1x15贝斯箱体。 | E | 模型未提供理由，需复核 |
| 31561 | A boutique ported 2x12 bass cab. | 一款精品倒相式 2x12 贝斯音箱。 | 一款精品倒相式 2x12 贝斯箱体。 | E | 模型未提供理由，需复核 |
| 31563 | A boutique 4x10 bass cab. | 一款精品 4x10 贝斯音箱。 | 一款精品 4x10 贝斯箱体。 | E | 根据已落地术语，cab 应译为“箱体”，现译“音箱”不准确。 |
| 31567 | A classic ported 2x10 cab. | 一款经典倒相式 2x10 音箱。 | 一款经典倒相式 2x10 箱体。 | E | 规则11：cab 应译为箱体，而非音箱。 |
| 31569 | A classic 4x10 alloy speaker cab. | 一款经典 4x10 合金扬声器音箱。 | 一款经典 4x10 合金扬声器箱体。 | E | 模型未提供理由，需复核 |
| 31571 | A unique 3x12 folded bass cab. | 独特的 3x12 折叠式贝斯音箱。 | 独特的 3x12 折叠式贝斯箱体。 | E | cab 应译为箱体 |
| 31573 | A classic folded 1x15 bass cab. | 一款经典折叠式 1x15 贝斯音箱。 | 一款经典折叠式 1x15 贝斯箱体。 | E | 模型未提供理由，需复核 |
| 31575 | A custom 1x12 bass cab. | 一款定制 1x12 贝斯音箱。 | 一款定制 1x12 贝斯箱体。 | E | cab 应译为箱体，而非音箱 |
| 31580 | EPIPHONE® ELECTAR "HAWAIIAN" CAB | EPIPHONE® ELECTAR "HAWAIIAN" 音箱 | EPIPHONE® ELECTAR "HAWAIIAN" 箱体 | E | 模型未提供理由，需复核 |
| 31581 | An 8-inch open-back combo. | 一款8英寸开放式背板组合音箱。 | 一款8英寸开放式背板一体式音箱。 | E | 模型未提供理由，需复核 |
| 31583 | A 10-inch open-back combo. | 一款 10 英寸开放式背板组合音箱。 | 一款 10 英寸开放式背板一体式音箱。 | E | 规则11：设备结构专用词义，combo 应译为“一体式音箱”，现译“组合音箱”不符合已落地术语。 |
| 31585 | A 12-inch closed-back combo. | 一款 12 英寸封闭式箱体组合音箱。 | 一款 12 英寸封闭式一体式音箱。 | E | 根据规则11，combo 译为“一体式音箱”，现译“箱体组合音箱”不准确。 |
| 31586 | EPIPHONE® "ZEPHYR" CAB | EPIPHONE® "ZEPHYR" 音箱 | EPIPHONE® "ZEPHYR" 箱体 | E | 模型未提供理由，需复核 |
| 31587 | A 15-inch open-back combo. | 一款15英寸开放式背板组合音箱。 | 一款15英寸开放式背板一体式音箱。 | E | combo 应译为一体式音箱 |
| 31593 | An open-back 12-inch combo cab. | 开放式背板 12 英寸组合音箱。 | 开放式背板 12 英寸一体式音箱。 | E | combo 应译为'一体式音箱'，原译'组合音箱'不符合已落地术语 combo=一体式音箱。 |
| 31595 | A classic Orange 4x12 cab. | 一款经典 Orange 4x12 音箱。 | 一款经典 Orange 4x12 箱体。 | E | 模型未提供理由，需复核 |
| 31597 | A compact closed-backed Orange 2x12 cab. | 一款紧凑型封闭式背板 Orange 2x12 音箱。 | 一款紧凑型封闭式背板 Orange 2x12 箱体。 | E | 根据规则11，cab 译为“箱体”，现译“音箱”不准确。 |
| 31599 | A vintage Orange 4x12 cab for a "Jimmy Bean" amp. | 复古 Orange 4x12 音箱，用于 "Jimmy Bean" 音箱头。 | 复古 Orange 4x12 箱体，用于 "Jimmy Bean" 音箱头。 | E | cab 应译为箱体，而非音箱 |
| 31603 | A vintage Marshall 4x12 cab. | 一款复古Marshall 4x12音箱柜。 | 一款复古 Marshall 4x12 箱体。 | E | 模型未提供理由，需复核 |
| 31607 | A Closed-back Marshall 1x12 cab. | 一款封闭式 Marshall 1x12 音箱柜。 | 一款封闭式 Marshall 1x12 箱体。 | E | cab 应译为箱体，而非音箱柜 |
| 31617 | A Cali-style 2x15 cab. | 一款加州风格的 2x15 音箱。 | 一款加州风格的 2x15 箱体。 | E | 根据已落地术语，cab 应译为“箱体”，现译“音箱”不准确。 |
| 31625 | A rare vintage 2x15 cab. | 一款稀有的复古2x15音箱。 | 一款稀有的复古2x15箱体。 | E | 根据规则11，cab应译为“箱体” |
| 31639 | A modern ported 2x15 cab. | 一款现代倒相式2x15音箱柜。 | 一款现代倒相式2x15箱体。 | E | cab 已落地术语为“箱体” |
| 31641 | A modern half-open half-closed 2x12. | 现代半开放式半封闭式 2x12 音箱。 | 现代半开放式半封闭式 2x12 箱体。 | E | 规则11：cab 应译为箱体，而非音箱。 |
| 31649 | A US yellow-style open-back 1x10. | 一款美式黄色风格的开放式背板 1x10 音箱。 | 一款美式黄色风格的开放式背板 1x10 箱体。 | E | 规则11：cab 应译为箱体，而非音箱。 |
| 31775 | • Make sure the USB end of your Rocksmith Real Tone Cable is plugged into a USB port on the console{C} system{C} or comp | • 请确保 Rocksmith Real Tone Cable 的 USB 端已插入主机的 USB 端口{C} 系统{C} 或您正在使用的电脑。 | • 请确保 Rocksmith Real Tone Cable 的 USB 端已插入主机{C}系统{C}或您正在使用的电脑的 USB 端口。 | E | 模型未提供理由，需复核 |
| 34026 | Select an Authentic Tone in Tone Designer. | 在音色设计师中选择一个真实音色。 | 在音色设计师中选择一个原曲音色。 | E | 规则14：Authentic Tone 统一译为原曲音色。 |
| 34840 | Zoom Out = D-pad down | 缩小 = 方向键下 | 缩小 = 十字键下 | E | D-pad 应统一译为十字键 |
| 34846 | Tempo Decrease = D-pad left | 速度减慢 = 方向键左 | 速度减慢 = 十字键左 | E | D-pad 应统一译为十字键，而非方向键 |
| 34991 | Combo! | 连击！ | 一体式音箱！ | E | 根据规则11，combo 在设备语境下应译为一体式音箱，而非连击。 |
| 35366 | New skins are now available for this cabinet. | 该机柜现已提供新皮肤。 | 该箱体现已提供新皮肤。 | E | 根据已落地术语，cabinet 在此语境下指音箱箱体，应译为“箱体”而非“机柜”。 |
| 35373 | An Eden compact bass head. | Eden 紧凑型贝斯头。 | Eden 紧凑型贝斯音箱头。 | E | head 指人体头部时不译音箱头，但此处 'bass head' 明确指贝斯音箱头，根据已落地术语 head=音箱头，原译'贝斯头'错误，应为'贝斯音箱头'。 |
| 35375 | An Eden 1x15 with HF driver. | 配备高频驱动器的 Eden 1x15 音箱。 | 配备高频扬声器单元的 Eden 1x15 音箱。 | E | 原文 HF driver 指高频扬声器单元（speaker driver），现译“高频驱动器”易误解为电子驱动电路，且违反规则11中 speaker driver=扬声器单元的术语约定。 |
| 35377 | An Eden 4x10 with HF driver. | 配备高频扬声器的Eden 4x10音箱。 | 配备高频扬声器单元的 Eden 4x10 音箱。 | E | HF driver 应译为“高频扬声器单元” |
| 35378 | An Eden high-power 6x10 with HF driver. | 配备高频扬声器的Eden高功率6x10音箱。 | 配备高频扬声器单元的Eden高功率6x10箱体。 | E | 根据规则11，speaker driver应译为“扬声器单元”，且cab在设备语境下应译为“箱体”而非“音箱”（amp才是音箱） |
| 35379 | A classic ‘punchy’ 4x10 bass cab. | 一款经典“有力”的 4x10 贝斯音箱。 | 一款经典“有力”的 4x10 贝斯箱体。 | E | cab 应译为箱体，而非音箱 |
| 35731 | Flanger | 相位器 | 颤音器 | E | Flanger 标准译名为颤音器，相位器对应 Phaser |
| 36853 | In Microphone Mode{C} you can play your guitar into a USB microphone connected to your console or computer. This is a gr | 在麦克风模式下{C} 你可以对着连接到主机或电脑的 USB 麦克风演奏吉他。这是没有拾音器的原声吉他玩家的绝佳选择。你的吉他不会经过 Rocksmith 2014 的真实音色处理{C} 但在演奏歌曲时仍会正常计分。麦克风模式下不支持多人游戏 | 在麦克风模式下{C} 你可以对着连接到主机或电脑的 USB 麦克风演奏吉他。这是没有拾音器的原声吉他玩家的绝佳选择。你的吉他不会经过 Rocksmith 2014 的原曲音色处理{C} 但在演奏歌曲时仍会正常计分。麦克风模式下不支持多人游戏 | E | 根据已落地术语，Authentic Tone 应译为“原曲音色”，现译“真实音色”不符合术语规范。 |

### 桶 F（21）

| id | source | original | revised | 分类 | reason |
|---|---|---|---|---|---|
| 6104 | The save game you tried to load is either missing or corrupt.  A backup save game is available{C} do you want to load it | 您尝试加载的存档缺失或已损坏。有一个备份存档可用{C}您想改为加载它吗？ | 你尝试加载的存档缺失或已损坏。有一个备份存档可用{C}你想改为加载它吗？ | F | 根据规则5，玩家代词应统一使用“你”，原译“您”不符合规范。 |
| 6141 | Your device does not have enough space to create a save game | 您的设备空间不足，无法创建存档 | 你的设备空间不足，无法创建存档 | F | 统一使用“你”作为玩家代词，原译“您的”不符合规则5 |
| 6234 | A sign-in change occurred.  You are now being returned to the title screen. | 登录状态已更改。您现在将返回标题界面。 | 登录状态已更改。你将被返回标题界面。 | F | 原文 'You are now being returned' 为被动语态，现译 '您现在将返回' 易被误解为玩家主动操作，且 '您' 不符合玩家用 '你' 的规范，改为 '你将被返回' 更准确。 |
| 6331 | No storage device has been selected. Your progress and settings will not be saved. | 未选择存储设备。您的进度和设置将不会被保存。 | 未选择存储设备。你的进度和设置将不会被保存。 | F | 统一使用“你”作为玩家代词，原译“您的”不符合规则5 |
| 6332 | No storage device has been selected. Your progress and settings will not be saved. | 未选择存储设备。您的进度和设置将不会被保存。 | 未选择存储设备。你的进度和设置将不会被保存。 | F | 统一使用“你”作为玩家代词，符合规则5及语境一致性 |
| 7079 | Game data is corrupt. Exit the game and then restart after deleting [Name of the Game] game data. | 游戏数据已损坏。请退出游戏，删除[游戏名称]的游戏数据后重新启动。 | 游戏数据已损坏。请退出游戏，删除 [Name of the Game] 的游戏数据后重新启动。 | F | 源文本占位符为 [Name of the Game]，译文误译为中文描述 [游戏名称]，违反占位符原样保留规则。 |
| 7085 | Failing to free the required space will prevent the game from saving your settings and your progress. | 如果无法释放所需空间，游戏将无法保存您的设置和进度。 | 如果无法释放所需空间，游戏将无法保存你的设置和进度。 | F | 统一使用“你”作为玩家代词，符合规则5及语境一致性 |
| 7138 | Saving… Please don't turn off your system. | 正在保存… 请勿关闭系统。 | 正在保存……请勿关闭系统。 | F | 源文本使用英文省略号 '...'，中文规范应使用 '……'，且原译文省略号后有多余空格，需修正排版。 |
| 7142 | There is insufficient free space on the HDD. This game requires at least [proper Size to put here] MB to save data. Plea | HDD上的可用空间不足。此游戏至少需要[此处应填入正确大小] MB来保存数据。请退出游戏，在HDD上腾出更多空间后重新启动。 | HDD 上的可用空间不足。此游戏至少需要 [proper Size to put here] MB 来保存数据。请退出游戏，在 HDD 上腾出更多空间后重新启动。 | F | 源文本占位符为 [proper Size to put here]，译文误译为中文描述 [此处应填入正确大小]，违反占位符原样保留规则。 |
| 7161 | Failing to free the required space will prevent the game from saving your settings and your progress. | 如果无法释放所需空间，游戏将无法保存您的设置和进度。 | 如果无法释放所需空间，游戏将无法保存你的设置和进度。 | F | 原文使用 your，根据规则5玩家用你，现译误用“您的” |
| 7281 | Failing to free the required space will prevent the game from saving your settings and your progress. | 如果无法释放所需空间，游戏将无法保存您的设置和进度。 | 如果无法释放所需空间，游戏将无法保存你的设置和进度。 | F | 统一使用“你”作为玩家代词，原译“您的”不符合规则5 |
| 17569 | Rocksmith offers a collection of minigames to build your guitar skills. Your first game is available in the Guitarcade{C | Rocksmith 提供一系列小游戏来锻炼您的吉他技巧。您的第一个游戏可在吉他街机中获取{C}，现在可从主菜单访问。 | Rocksmith 提供一系列小游戏来锻炼你的吉他技巧。你的第一个游戏可在吉他街机中获取{C}，现在可从主菜单访问。 | F | 根据规则5，玩家代词应统一使用“你”，原译“您的”不符合规范。 |
| 17574 | You can also save audio replays manually{C} at the end of each song. | 你也可以手动保存音频回放{C} 在每首歌曲结束时。 | 你也可以在每首歌曲结束时手动保存音频回放{C}。 | F | 原译“在每首歌曲结束时”置于句末导致语序生硬，且占位符{C}后紧跟中文逗号不符合中文排版习惯，调整语序使句子更通顺自然。 |
| 17720 | Rocksmith will continue to track your progress as you play. You can continue to advance your skills by downloading new m | Rocksmith 将在您游玩时持续追踪您的进度。您可以在 Best Buy 商店下载新音乐以继续提升技巧。 | Rocksmith 将在你游玩时持续追踪你的进度。你可以在 Best Buy 商店下载新音乐以继续提升技巧。 | F | 统一使用“你”作为玩家代词，符合规则5及语境一致性 |
| 17749 | Rocksmith will continue to track your progress as you play. You can continue to advance your skills by downloading new m | Rocksmith 将在您游玩时持续追踪您的进度。您可以在 Best Buy 旗下的 Rocksmith 商店下载新音乐以继续提升技巧。 | Rocksmith 将在你游玩时持续追踪你的进度。你可以在 Best Buy 旗下的 Rocksmith 商店下载新音乐以继续提升技巧。 | F | 规则5要求玩家用“你”，原译误用“您” |
| 20310 | Tip: Add or remove songs from your Event setlist in the Customize option in the Event Manager menu … | 提示：在事件管理器菜单的自定义选项中添加或移除活动歌单中的歌曲…… | 提示：在活动管理菜单的自定义选项中添加或移除活动歌单中的歌曲…… | F | 规则13规定event(活动)译为活动，原译“事件管理器”错误 |
| 21164 | press the cross button | 按十字键 | 按叉键 | F | cross button 是 PlayStation 的叉形按钮，应译为“叉键”而非“十字键” |
| 21756 | You can access all your open events in the Event Manager menu. | 您可以在活动管理菜单中查看所有未结束的活动。 | 你可以在活动管理菜单中查看所有未结束的活动。 | F | 规则5要求玩家用“你”，原译误用“您” |
| 22647 | To play Emulated Bass{C} please first properly calibrate and setup your guitar by selecting Guitar instead of Bass.  {L} | 要演奏模拟贝斯{C} 请先选择吉他而非贝斯，正确校准并设置您的吉他。  {L}{L}完成声音检查后{C} 您可以在主菜单中选择“开始贝斯之旅”来演奏模拟贝斯。 | 要演奏模拟贝斯{C} 请先选择吉他而非贝斯，正确校准并设置你的吉他。  {L}{L}完成声音检查后{C} 你可以在主菜单中选择“开始贝斯之旅”来演奏模拟贝斯。 | F | 原文 'your guitar' 和 'you can play' 指代玩家，现译 '您的吉他' 和 '您' 不符合玩家用 '你' 的规范。 |
| 36185 | Uninstalling the latest patch will cause your save data to be incompatible with previous versions of Rocksmith. Do you w | 卸载最新补丁将导致您的存档数据与 Rocksmith 旧版本不兼容。您是否要覆盖并创建新的存档数据？ | 卸载最新补丁将导致你的存档数据与 Rocksmith 旧版本不兼容。你是否要覆盖并创建新的存档数据？ | F | 根据规则5，玩家代词应统一使用“你”，原译“您的”不符合规范。 |
| 37365 | Rocksmith will not evaluate your playing or adjust your difficulty as you play. You can adjust your difficulty manually  | Rocksmith 不会评估您的演奏或在游玩时自动调整难度。您可以使用乐句重复器或难度设置菜单手动调整难度。 | Rocksmith 不会评估你的演奏或在游玩时自动调整难度。你可以使用乐句重复器或难度设置菜单手动调整难度。 | F | 根据规则5，玩家代词应统一使用“你”，原译“您”不符合规范。 |

### 桶 G（36）

| id | source | original | revised | 分类 | reason |
|---|---|---|---|---|---|
| 7420 | Wave your RIGHT hand when you are ready to play! | 准备好演奏时，请挥动您的右手！ | 准备好演奏时，请挥动你的右手！ | G | 规则17及代词规则要求玩家用“你”，原译“您”不符合规范。 |
| 10103 | The key is that you always go down on downbeats and up on upbeats.  Even if you leave a note out{C} your hand still keep | 关键在于，重拍时手向下，轻拍时手向上。即使你省略了某个音符{C}你的手依然要保持上下运动，就像在那里弹了音符一样。 | 关键在于，正拍时手向下，反拍时手向上。即使你省略了某个音符{C}你的手依然要保持上下运动，就像在那里弹了音符一样。 | G | 规则7指出拨弦教学中 downbeat/upbeat 对应正拍及反拍，不宜机械译成强拍/弱拍或重拍/轻拍，原译“重拍/轻拍”不符合术语规范。 |
| 13239 | Then you just attach the other end to the other button. | 然后把另一端连接到另一个按钮上。 | 然后把另一端连接到另一个背带扣上。 | G | 原文 button 指代上一句的 strap buttons（背带扣），现译“按钮”易误解为电子按键，应统一为“背带扣”。 |
| 17562 | The Tracker charts your rise in skill as a guitar player. | 追踪器记录您作为吉他手技能的提升。 | 追踪器记录你作为吉他手技能的提升。 | G | 规则5要求玩家用“你”，原译“您”不符合规范 |
| 17715 | You have 1 open event. | 你有 1 个未结束的事件。 | 你有 1 个未结束的活动。 | G | 根据已落地术语，event(活动)应译为活动，而非事件 |
| 17736 | Completed Master Event | 完成大师事件 | 完成大师活动 | G | 根据已落地术语，event(活动)应译为活动，而非事件 |
| 17742 | You can retry the Event as many times as you need. | 你可以重试该事件任意次。 | 你可以重试该活动任意次。 | G | 根据已落地术语，event(活动)应译为活动，原译“事件”错误。 |
| 17821 | You've earned the ability to play with Authentic Song Tones. | 你已解锁使用真实歌曲音色的能力。 | 你已解锁使用原曲音色的能力。 | G | 根据已落地术语，Authentic Tone 应译为“原曲音色”，现译“真实歌曲音色”不符合术语规范。 |
| 17822 | You've earned the ability to play with Authentic Song Tones{C} taking your guitar sound to the next level. | 你已解锁使用真实歌曲音色的能力{C}将你的吉他音色提升至新的高度。 | 你已解锁使用原曲音色的能力{C}将你的吉他音色提升至新的高度。 | G | 根据已落地术语，Authentic Tone 应统一译为原曲音色，而非真实歌曲音色。 |
| 17823 | You've reached a new milestone{C} the ability to play with Authentic Song Tones. | 你达到了一个新的里程碑{C}使用真实歌曲音色的能力。 | 你达到了一个新的里程碑{C}使用原曲音色的能力。 | G | 根据已落地术语规则，Authentic Tone 应统一译为“原曲音色”，现译“真实歌曲音色”不符合术语规范。 |
| 19183 | Guitar Basics:{L}6-in-line Tuning Overview | 吉他基础：{L}六弦同调调弦概览 | 吉他基础：{L}六联排调弦概览 | G | 规则11及术语表规定 inline 译为“联排”，原译“同调”错误 |
| 20330 | Tip: To check your progress towards qualifying your songs for an Event{C} choose the Event Manager option on the Rocksmi | 提示：要查看歌曲在事件中的资格进度{C}请在 Rocksmith 推荐界面选择事件管理器选项…… | 提示：要查看歌曲在活动中的资格进度{C}请在 Rocksmith 推荐界面选择活动管理器选项…… | G | 根据已落地术语，event(活动)应译为活动，原译误译为事件 |
| 21766 | You've been invited to play at The Hangar.{L}{L}To access your suggested setlist for this venue{C} go to the Event Manag | 你被邀请去The Hangar演出。{L}{L}要访问这个Venue的建议歌单{C}请前往Event Manager。 | 你被邀请去 The Hangar 演出。{L}{L}要访问这个场地的建议歌单{C}请前往 Event Manager。 | G | 规则3要求品牌专名保留英文，但 'Venue' 在此处为普通名词（场地/场馆），非品牌名，应译为中文；'Event Manager' 为功能模块名，保留英文或译为“活动管理器”均可，但现译将 'Venue' 误作专名保留，且 'The Hangar' 前缺少空格（规则20）。 |
| 22017 | Congratulations! You just earned a new rank. | 恭喜！您刚刚获得了一个新等级。 | 恭喜！你刚刚获得了一个新等级。 | G | 规则要求玩家用“你”，现译误用“您”。 |
| 22251 | Slaps are performed with your thumb. | 击打是用拇指完成的。 | 拍弦是用拇指完成的。 | G | 根据已落地术语规则，Slap 应译为“拍弦”，现译“击打”不符合术语规范。 |
| 22259 | Try playing slaps and pops in the upcoming phrase. | 尝试在接下来的乐句中使用击弦和勾弦技巧。 | 尝试在接下来的乐句中使用拍弦和勾拍技巧。 | G | 规则5及已落地术语：Slap 应译为“拍弦”，Pop 应译为“勾拍”，原译“击弦”和“勾弦”不准确。 |
| 22425 | Syncopation may also result from accenting offbeat notes{C} even when there are also notes on the beats | 切分音也可能由重音落在弱拍音符上产生{C}即使强拍上也有音符 | 切分音也可能由重音落在反拍音符上产生{C}即使正拍上也有音符 | G | 根据规则7，offbeat 对应反拍，beats 对应正拍，原译“弱拍/强拍”混淆了节拍位置与强弱关系。 |
| 22428 | For slaps{C} use the side of your thumb’s knuckle | 对于拍击{C}请使用拇指指关节的侧面 | 对于拍弦{C}请使用拇指指关节的侧面 | G | 根据规则5，Slap 应译为“拍弦”，现译“拍击”不准确。 |
| 22444 | Octaves and Fifths are musical terms describing intervals{C} or the distance between two notes.  Both Octaves and Fifths | 八度和五度是描述音程的音乐术语{C}或两个音符之间的距离。八度和五度音程都很重要，且在贝斯线条中频繁出现。 | 八度和五度是描述音程的音乐术语{C}即两个音符之间的距离。八度和五度音程都很重要，且在贝斯线条中频繁出现。 | G | 原文 'or' 在此处为解释性用法（即），现译 '或' 易产生歧义，改为 '即' 更符合中文逻辑 |
| 22584 | Congratulations! You've unlocked Master Mode for this arrangement by scoring 100{C}000 and maxing out all phrases. Play  | 恭喜！你通过获得100分解锁了此编曲的大师模式{C}000并完美演奏所有乐句。在大师模式中演奏以证明你的贝斯技巧并获得最高分数。{L}{L}注意：当你解锁歌单中所有编曲的大师模式时，可以将任何活动变为大师活动。 | 恭喜！你通过获得100{C}000分并完美演奏所有乐句解锁了此编曲的大师模式。在大师模式中演奏以证明你的贝斯技巧并获得最高分数。{L}{L}注意：当你解锁歌单中所有编曲的大师模式时，可以将任何活动变为大师活动。 | G | 原译将占位符{C}错误地置于“100”和“000”之间，导致分数显示为“100分解锁...000”，破坏了数值逻辑；修正后将{C}移至“100”和“000”之间以正确表示100,000分，并调整语序使句子通顺。 |
| 22648 | Would you like to start your guitar journey? | 您想开始您的吉他之旅吗？ | 你想开始你的吉他之旅吗？ | G | 规则17及通用规范：玩家用“你”，原译“您”不符合代词规范。 |
| 22683 | Please make sure you are on an electric guitar and not a bass guitar. | 请确保您使用的是电吉他，而不是贝斯。 | 请确保你使用的是电吉他，而不是贝斯。 | G | 根据规则5，玩家代词应统一使用“你”，原译“您”不符合规范。 |
| 22873 | This demo includes one of Rocksmith’s eight minigames designed to enhance your guitar skills. | 此演示包含 Rocksmith 八款迷你游戏之一，旨在提升您的吉他技巧。 | 此演示包含 Rocksmith 八款迷你游戏之一，旨在提升你的吉他技巧。 | G | 规则5要求玩家用你，原译误用您的 |
| 23521 | So{C} this one is an open A. | 所以{C} 这个是一个空弦 A。 | 所以{C} 这是一个空弦 A。 | G | 模型未提供理由，需复核 |
| 25473 | Mix some muted notes into your slapping to give it that classic percussive sound. | 在击弦中加入一些闷音，以营造经典的打击乐效果。 | 在拍弦中加入一些闷音，以营造经典的打击乐效果。 | G | 原文 slapping 对应贝斯拍弦技法，现译“击弦”易与吉他击弦（Tapping）混淆，应统一为“拍弦”。 |
| 26856 | Change the Complexity to Progressive. | 将难度更改为渐进式。 | 将复杂度更改为渐进式。 | G | 术语统一：Complexity 应译为“复杂度”而非“难度” |
| 27712 | …and It Wasn't a Fluke | …and It Wasn't a Fluke | ……而且这不是侥幸 | G | source 为英文标题，translation 未翻译，违反使用简体中文的规则。 |
| 27777 | Slaps look like this: | 击打看起来像这样： | 拍弦看起来像这样： | G | 根据已落地术语，Slap 应译为“拍弦”，现译“击打”不符合术语规范。 |
| 29138 | Keep [1] Happy for [2] minutes. | 保留 [1] Happy 为 [2] 分钟。 | 让 [1] Happy 保持 [2] 分钟。 | G | 原文 Keep [1] Happy 意为使对象保持快乐状态，现译“保留...为”语义错误且不通顺。 |
| 30235 | ALTERNATIVE CARTRIDGE | 另类卡带 | 替代卡带 | G | ALTERNATIVE 在此语境下指“替代/备用”而非“另类”，现译“另类”语义偏差。 |
| 32216 | Slice a ghost for the first time. | 首次消除幽灵。 | 首次消除幽灵音符。 | G | 根据规则10，ghosted notes 是淡化显示的音符，即幽灵音符，原译“幽灵”指代不明。 |
| 32302 | Pass [1] lines of cars while in a red lane. | 超越[1]条车线，且处于红色车道。 | 在红色车道中超越[1]条车线。 | G | 原文 'while in a red lane' 是条件状语，现译 '且处于' 逻辑关系错误，应为 '在...中' 或 '当...时'。 |
| 32304 | Pass [1] lines of cars while in a blue lane. | 超越[1]条车线，且处于蓝色车道。 | 在蓝色车道中超越[1]条车线。 | G | 原文 'while in a blue lane' 表示动作发生的条件/状态，现译 '且处于' 逻辑生硬且未体现伴随状态，改为 '在...中' 更符合中文习惯及语境逻辑。 |
| 34339 | When you've played this song before{C} it's sounded like you might need a hand with your [1]. You can get a solid handle | 如果你之前演奏过这首歌{C}听起来你可能需要在你的  方面需要帮助。[1]你可以将乐句重复器设置为加速模式，通过演奏这个乐句来熟练掌握它们。 | 如果你之前演奏过这首歌{C}听起来你可能需要在[1]方面需要帮助。你可以将乐句重复器设置为加速模式，通过演奏这个乐句来熟练掌握它们。 | G | 原文 'need a hand with your [1]' 中 [1] 为占位符，现译在 [1] 前错误插入了空格，且 'in your [1]' 结构对应中文 '在[1]方面'，需去除占位符前的多余空格以符合排版规范。 |
| 34674 | Last time you tried out the frethand mutes in this song{C} it sounded like you almost hit them all perfectly. Great job! | 上次尝试这首歌中的左手闷音时{C} 听起来你几乎全部完美命中。干得漂亮！试试 Hurtlin' Hurdles 来热身。这会让练习左手闷音变得有趣{C} 之后你就能在歌曲中掌握它们了。 | 上次尝试这首歌中的左手制音时{C} 听起来你几乎全部完美命中。干得漂亮！试试 Hurtlin' Hurdles 来热身。这会让练习左手制音变得有趣{C} 之后你就能在歌曲中掌握它们了。 | G | 根据已落地术语，fret-hand mute 应译为“左手制音”而非“左手闷音” |
| 37029 | Please wait while we untangle some cords... | 请稍候，我们正在整理线缆... | 请稍候，我们正在整理线缆…… | G | 原文使用省略号，中文规范应使用“……”而非半角点 |
