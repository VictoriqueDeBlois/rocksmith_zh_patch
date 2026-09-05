# 设置翻译复核（2026-09-05）

依据：当前游戏 localization/maingame.csv 的英文原文及相邻设置说明。复核范围：画面与高级画面设置、音频设置、演奏与难度设置。以下只列修改项，不代表全游戏文本复核。

修订写入 config/overrides.json；保留 legacy 与 proofread_manual 源数据。Venue Mode 的含义由原文 29037 直接确认：关闭舞台特效后，演奏背景保留在阁楼。

| ID | 英文原文 | 修改前 | 修改后 |
| --- | --- | --- | --- |
| 22739 | Visual Quality | 视觉质量 | 画面质量 |
| 23379 | Visual Quality | 视觉质量 | 画面质量 |
| 22807 | You must restart Rocksmith for this setting to apply. | 你必须重新启动游戏套用保存这个装置的设定. | 重启游戏后，此设置才会生效。 |
| 28779 | AUDIO SETTINGS | 音频设定 | 音频设置 |
| 28780 | VISUAL SETTINGS | 视觉设定 | 画面设置 |
| 28781 | PLAY SETTINGS | 玩家设定 | 演奏设置 |
| 28783 | RESTORE DEFAULT OPTIONS | 回复预设值 | 恢复默认设置 |
| 28821 | MICROPHONE SETTINGS | 麦克风设定 | 麦克风设置 |
| 28825 | AUDIO ENGINE SETTINGS | 音频引擎设定 | 音频引擎设置 |
| 28829 | Enable for singing. | 启用歌唱. | 启用麦克风演唱功能。 |
| 28831 | AUDIO EXCLUSIVITY | 专用音频 | 音频独占 |
| 28832 | Enable to give Rocksmith 2014 exclusive control of PC audio. | 启用给 Rocksmith 2014 专用的音频使用权. | 允许 Rocksmith 2014 独占电脑的音频设备。 |
| 28833 | VISUAL SETTINGS | 视觉设定 | 画面设置 |
| 28839 | SCREEN POSITION | 荧幕位置 | 屏幕位置 |
| 28850 | GAMEPLAY SETTINGS | 游戏玩法设定 | 演奏设置 |
| 28864 | SET ALL SONG DIFFICULTY | 设定所有歌曲难度 | 设置所有歌曲难度 |
| 28866 | MICROPHONE SETTINGS | 麦克风设定 | 麦克风设置 |
| 28867 | AUDIO ENGINE SETTINGS | 音频引擎设定 | 音频引擎设置 |
| 28868 | AUDIO EXCLUSIVITY | 专用音频 | 音频独占 |
| 28870 | SCREEN POSITION | 荧幕位置 | 屏幕位置 |
| 28877 | 6-inline | 6 联排 | 六弦钮单排 |
| 28881 | 4 in line | 4 连音 | 四弦钮单排 |
| 28886 | EMULATE BASS | 仿真贝斯 | 模拟贝斯 |
| 28895 | EMULATE BASS | 仿真贝斯 | 模拟贝斯 |
| 28897 | VENUE MODE | 地点模式 | 舞台模式 |
| 28899 | VISUAL QUALITY | 视觉品质 | 画面质量 |
| 28900 | WINDOWED MODE | 视窗模式 | 窗口模式 |
| 28903 | VENUE MODE | 地点模式 | 舞台模式 |
| 28908 | Mild | 中度 | 轻度 |
| 28909 | Extreme | 强度 | 重度 |
| 28911 | VISUAL QUALITY | 视觉品质 | 画面质量 |
| 28916 | WINDOWED MODE | 视窗模式 | 窗口模式 |
| 28918 | Windowed | 视窗 | 窗口 |
| 28925 | RESET OPTIONS | 重新设定 | 恢复默认设置 |
| 29037 | Disable or enable all Venue effects. The Loft will remain the background during songs instead of your progress opening a portal to the venue. | 关闭或开启所有环境的影响. 阁楼将保持在歌曲的背景 而不是因你的进步打开一个门户到会场. | 开启或关闭舞台特效。关闭后，演奏时的背景会一直保留在练习阁楼，不再随着演奏进展打开通往舞台的入口。 |
| 29040 | Change all settings and options back to their original states. | 将所有设定和选项回复到原始的状态. | 将所有设置和选项恢复为默认值。 |
| 29043 | Pick which hand will strum and pluck. | 选择哪只手持弹片弹奏. | 选择用哪只手扫弦和拨弦。 |
| 29044 | Switch the string interface so that the low E is displayed as the string closest to the bottom of the screen. | 反转琴弦的配置位置让 E 弦的位置显示在荧幕的最下方. | 反转屏幕上的琴弦排列，使低音 E 弦显示在最下方。 |
| 29045 | Turn Master Mode Off to view the notes in riffs you've already Mastered. Choose On to have the notes fade in and out as you Master a song. | 关闭大师模式时你可以看着音符即兴演奏.开启后当你已经掌握一首乐曲时音符将淡入或淡出. | 关闭大师模式后，已掌握的乐句仍会显示音符。开启后，音符会随歌曲的掌握程度淡入淡出。 |
| 29046 | Enable to to play bass arrangements on the lowest four strings of your guitar. | 启用玩贝斯并安排你的吉他上最低的四根弦. | 启用后，可用吉他上音高最低的四根弦演奏贝斯声部。 |
| 29047 | Disable or enable the number displays on the chord fingerprints. | 启用或禁用和弦指纹上的数字显示。 | 开启或关闭和弦指型图中的手指编号。 |
| 29056 | Turn off Master Mode to view the notes in riffs you've already mastered. Choose Alternate to have the notes fade in and out. | 关闭主模式以查看已掌握的乐句中的音符。选择“交替”可使音符淡入淡出。 | 关闭大师模式后，已掌握的乐句仍会显示音符。选择“交替”可使音符淡入淡出。 |
| 36632 | ADV DISPLAY SETTINGS | 进阶显示设定 | 高级画面设置 |
| 36633 | ADV DISPLAY SETTINGS | 进阶显示设定 | 高级画面设置 |
| 36634 | Adjusts the overall graphical quality of the game. | 调整游戏的整体图形品质. | 调整游戏的整体画面质量。 |
| 36635 | Custom | 自制 | 自定义 |
| 36636 | Non-Exclusive Fullscreen | 非全屏专用 | 非独占全屏 |
| 36637 | Exclusive Fullscreen | 全屏 | 独占全屏 |
| 36643 | PER-PIXEL LIGHTING | 像素明暗分布 | 逐像素光照 |
| 36644 | HIGH-RES SCOPE | 高解析范围 | 高清示波器 |
| 36645 | MSAA SETTING | MSAA 设定 | 多重采样抗锯齿 |
| 36649 | Once every 2 weeks{C} launch the Rocksmith 2014 website after exiting the game. | 当你退出游戏后启动摇滚史密斯 2014 网站{C} 每周2次. | 每两周一次{C} 在退出游戏后打开 Rocksmith 2014 网站。 |
| 36650 | Run Rocksmith 2014 at a low resolution. On large monitors{C} this will help improve frame rate and performance. Note that this is not the same as screen resolution unless Automatic is selected for Resolution. | 以较低的分辨率运作摇滚史密斯 2014. 在大型荧幕上{C} 这将有助于提高帧速率和性能. 请注意这是不一样的荧幕分辨率除非选择自动分辨率. | 以较低的渲染分辨率运行游戏。在大屏幕上{C} 这有助于提高帧率和运行性能。注意：渲染分辨率与屏幕分辨率不同，除非分辨率选项设为“自动”。 |
| 36651 | Controls the display of Bloom{C} Glow{C} Color Correction{C} and Depth of Field. Disabling this setting removes all of these effects{C} improving performance. | 控制 Bloom{C} Glow{C} 色彩校正{C} 和景深显示. 停用该设定会删除所有的影响{C} 可以提高性能. | 控制泛光{C} 辉光{C} 色彩校正{C} 和景深效果。关闭此设置会禁用这些特效{C} 提高运行性能。 |
| 36652 | Controls the game's Shadow effects. Disabling this effect removes dynamic Shadows{C} improving performance. | 控制游戏中的阴影效果. 如果关闭此效果会消除动态阴影{C} 并且提高性能. | 控制游戏的阴影效果。关闭后会禁用动态阴影{C} 提高运行性能。 |
| 36653 | Controls the Depth of Field effect. Disabling this removes Depth of Field{C} improving performance. | 控制景深效果. 如果停用删除景深效果{C} 可以提高性能. | 控制景深效果。关闭后会禁用景深{C} 提高运行性能。 |
| 36654 | Controls the game's lighting calculations. Disabling this setting reduces lighting quality and improves performance. | 控制游戏中的亮度计算. 如果关闭此设置会减少亮度质量并且提高性能. | 控制游戏的光照计算。关闭后会降低光照质量，提高运行性能。 |
| 36655 | Controls the oscillator scope within the game. Disabling this setting doesn't draw the oscillator during gameplay{C} improving performance. | 控制游戏中的高解析范围. 如果停用此设定在游戏过程中将不会有高解析{C} 可以提高性能. | 控制游戏中的示波器显示。关闭后，演奏时不再绘制示波器波形{C} 提高运行性能。 |
| 36656 | Controls the multi-sample anti-aliasing. Disabling this setting lowers the visual quality of the game{C} improving performance. | 控制多重采样反锯齿. 停用该设定会降低游戏的视觉质量{C} 可以提高性能. | 控制多重采样抗锯齿。关闭后会降低画面质量{C} 提高运行性能。 |
| 36659 | USB audio output devices can have performance issues such as audio crackling and increased latency. Consider using an onboard audio device or PCI/PCI-E based audio device. | USB的音频输出装置会有性能上的问题.例如杂音以及延迟上的问题. Consider using an onboard audio device or PCI/PCI-E based audio device. | USB 音频输出设备可能出现爆音、延迟增加等性能问题。可考虑使用板载声卡或 PCI/PCI-E 声卡。 |
| 36660 | Your computer does not have an audio output device. Install a sound card so you can hear the game. | 你的电脑没有音频输出装置. 你必须安装声卡驱动才能听到游戏声音. | 电脑没有音频输出设备。请安装声卡，以便播放游戏声音。 |
| 36663 | Your audio device is using a WDM driver. Configuring the game to use PortAudio may provide a better experience. | 你的音频设备使用WDM的驱动程序. Configuring the game to use PortAudio may provide a better experience. | 音频设备正在使用 WDM 驱动。将游戏配置为使用 PortAudio 可能会改善体验。 |
| 36664 | Your audio device is using a DirectSound driver.  Configuring the game to use PortAudio may provide a better experience. | 你的音频设备使用的是DirectSound驱动程序.  Configuring the game to use PortAudio may provide a better experience. | 音频设备正在使用 DirectSound 驱动。将游戏配置为使用 PortAudio 可能会改善体验。 |
| 36665 | Another audio device has exclusive control of your audio output device. Shut down that application and restart Rocksmith 2014. | 另一个音频设备有音频输出的独占控制权. Shut down that application and restart Rocksmith 2014. | 其他音频设备已独占你的音频输出设备。请关闭占用它的应用程序，再重启 Rocksmith 2014。 |
| 36668 | Rocksmith 2014 has detected that you’re running a high-performance computer. We’ve applied preliminary visual settings to take advantage of your hardware. If you want to adjust your visual settings{C} visit the Options menu. | Rocksmith 2014 检测到你有一台高性能电脑正在运行. 我们已经初步将你的硬体优势应用在视觉设置中. 如果你要调整你的视觉设置{C} 请到选项目录里更改设置. | Rocksmith 2014 检测到你的电脑性能较高，已自动设置初始画质以利用硬件性能。如需调整画面设置{C} 请前往选项菜单。 |
| 36669 | Rocksmith 2014 has detected that your computer performs close to our minimum requirements. We’ve applied preliminary visual settings to try to maximize performance. If you want to adjust your visual settings{C} visit the Options menu. | 摇滚史密斯 2014 检测到你的电脑配备刚好符合我们的最低要求. 我们已经初步应用在视觉设置里试图用最大的限度提高性能. 如果你要调整你的视觉设置{C} 请到选项目录里更改设置. | Rocksmith 2014 检测到你的电脑接近最低配置要求，已自动设置初始画质以尽量提高运行性能。如需调整画面设置{C} 请前往选项菜单。 |
| 36670 | Rocksmith 2014 has detected that your computer may not have performance high enough to provide an optimal experience. We’ve lowered visual and game settings to maximize performance{C} but your system may not run well. Consider upgrading your computer for a better Rocksmith 2014 experience. | 摇滚史密斯 2014 检测到你的电脑性能可能不够高不足以提供最佳的体验. 我们已经降低了视觉和游戏设置以其最大限度地提高性能{C}但是你的系统还是有可能无法让游戏正常运行. 请考虑一下升级你的电脑来运行 Rocksmith 2014 的最佳体验. | Rocksmith 2014 检测到你的电脑性能可能不足以提供最佳体验。游戏已降低画面和演奏设置以尽量提高运行性能{C} 但仍可能运行不畅。升级电脑可改善游戏体验。 |
| 36671 | Rocksmith 2014 has detected your computer is running at a low framerate{C} despite being set to minimal visual and game settings. You can improve performance by reducing the visual resolution and running in windowed mode. Visit the Options menu to change your settings. | 摇滚史密斯 2014 检测到你的电脑正在以较低的解析度运作{C} 就算被设置为最小视觉的游戏设置. 你还是可以透过视窗模式降低视觉分辨率已改进游戏运作的效能. 请到选项目录里更改设置. | Rocksmith 2014 检测到，即使画面和演奏设置已调至最低，游戏帧率仍然偏低{C} 可尝试降低渲染分辨率并使用窗口模式来提高运行性能。请前往选项菜单调整设置。 |
| 36898 | LEVEL UP SPEED | 升级速度 | 难度提升速度 |
| 36900 | LEVEL DOWN SPEED | 降低速度 | 难度降低速度 |
| 36904 | OVERRIDE TO MAX | 覆盖至最大 | 强制最高难度 |
| 36905 | Sets all arrangements to maximum difficulty. Automatic Leveling is OFF. | 将所有编曲设置为最高难度。自动等级已关闭。 | 将所有编曲设为最高难度，并关闭自动难度调整。 |
| 36907 | Sets Difficulty Settings to default: Dynamic Difficulty - ON{C} Leveling Speed - NORMAL{C} Sightreading Level - AUTO. | 将难度设置恢复为默认值：动态难度 - 开启{C} 升级速度 - 正常{C} 视奏等级 - 自动。 | 将难度设置恢复为默认值：动态难度开启{C} 难度变化速度正常{C} 视奏等级自动。 |
| 36910 | Override to Max: | 强制设为最大： | 强制最高难度： |
| 36912 | Level Up Speed: | 提升速度等级： | 难度提升速度： |
| 36913 | Level Down Speed: | 降低速度等级： | 难度降低速度： |
| 36938 | LEVEL UP SPEED | 升级速度 | 难度提升速度 |
| 36939 | LEVEL DOWN SPEED | 降低速度 | 难度降低速度 |
