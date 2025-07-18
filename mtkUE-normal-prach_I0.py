import re
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import numpy as np
import statistics

# 設定中文字體支援
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']  # 設定字體優先順序
plt.rcParams['axes.unicode_minus'] = False  # 正確顯示負號

log_data = """
[PHY]   [RAPROC] 565.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 566.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 567.19 prach_I0 = 17.6 dB
[PHY]   [RAPROC] 568.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 569.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 570.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 571.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 572.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 573.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 574.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 575.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 576.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 577.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 578.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 579.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 580.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 581.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 582.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 583.19 prach_I0 = 17.6 dB
[PHY]   [RAPROC] 584.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 585.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 586.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 587.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 588.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 589.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 590.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 591.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 592.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 593.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 594.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 595.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 596.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 597.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 598.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 599.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 600.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 601.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 602.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 603.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 604.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 605.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 606.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 607.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 608.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 609.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 610.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 611.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 612.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 613.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 614.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 615.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 616.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 617.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 618.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 619.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 620.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 621.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 622.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 623.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 624.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 625.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 626.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 627.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 628.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 629.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 630.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 631.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 632.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 633.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 634.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 635.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 636.19 prach_I0 = 17.6 dB
[PHY]   [RAPROC] 637.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 638.19 prach_I0 = 17.4 dB
[NR_MAC]   Frame.Slot 640.0

[PHY]   [RAPROC] 639.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 640.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 641.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 642.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 643.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 644.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 645.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 646.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 647.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 648.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 649.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 650.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 651.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 652.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 653.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 654.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 655.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 656.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 657.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 658.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 659.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 660.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 661.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 662.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 663.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 664.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 665.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 666.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 667.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 668.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 669.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 670.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 671.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 672.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 673.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 674.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 675.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 676.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 677.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 678.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 679.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 680.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 681.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 682.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 683.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 684.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 685.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 686.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 687.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 688.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 689.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 690.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 691.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 692.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 693.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 694.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 695.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 696.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 697.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 698.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 699.19 prach_I0 = 18.5 dB
[PHY]   [RAPROC] 700.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 701.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 702.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 703.19 prach_I0 = 18.5 dB
[PHY]   [RAPROC] 704.19 prach_I0 = 18.5 dB
[PHY]   [RAPROC] 705.19 prach_I0 = 18.5 dB
[PHY]   [RAPROC] 706.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 707.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 708.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 709.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 710.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 711.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 712.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 713.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 714.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 715.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 716.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 717.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 718.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 719.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 720.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 721.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 722.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 723.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 724.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 725.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 726.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 727.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 728.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 729.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 730.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 731.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 732.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 733.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 734.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 735.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 736.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 737.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 738.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 739.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 740.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 741.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 742.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 743.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 744.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 745.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 746.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 747.19 prach_I0 = 18.4 dB
[PHY]   [RAPROC] 748.19 prach_I0 = 18.6 dB
[PHY]   [RAPROC] 749.19 prach_I0 = 18.7 dB
[PHY]   [RAPROC] 750.19 prach_I0 = 18.5 dB
[PHY]   [RAPROC] 751.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 752.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 753.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 754.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 755.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 756.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 757.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 758.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 759.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 760.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 761.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 762.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 763.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 764.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 765.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 766.19 prach_I0 = 17.3 dB
[NR_MAC]   Frame.Slot 768.0

[PHY]   [RAPROC] 767.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 768.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 769.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 770.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 771.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 772.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 773.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 774.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 775.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 776.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 777.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 778.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 779.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 780.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 781.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 782.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 783.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 784.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 785.19 prach_I0 = 17.6 dB
[PHY]   [RAPROC] 786.19 prach_I0 = 17.6 dB
[PHY]   [RAPROC] 787.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 788.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 789.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 790.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 791.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 792.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 793.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 794.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 795.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 796.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 797.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 798.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 799.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 800.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 801.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 802.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 803.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 804.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 805.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 806.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 807.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 808.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 809.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 810.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 811.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 812.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 813.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 814.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 815.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 816.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 817.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 818.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 819.19 prach_I0 = 17.6 dB
[PHY]   [RAPROC] 820.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 821.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 822.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 823.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 824.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 825.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 826.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 827.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 828.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 829.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 830.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 831.19 prach_I0 = 17.6 dB
[PHY]   [RAPROC] 832.19 prach_I0 = 17.6 dB
[PHY]   [RAPROC] 833.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 834.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 835.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 836.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 837.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 838.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 839.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 840.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 841.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 842.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 843.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 844.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 845.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 846.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 847.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 848.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 849.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 850.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 851.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 852.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 853.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 854.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 855.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 856.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 857.19 prach_I0 = 17.6 dB
[PHY]   [RAPROC] 858.19 prach_I0 = 17.6 dB
[NR_PHY]    [RAPROC] 859.19 Initiating RA procedure with preamble 47, energy 56.4 dB (I0 176, thres 120), delay 0 start symbol 0 freq index 0
[PHY]   [RAPROC] 859.19 prach_I0 = 22.2 dB
[NR_MAC]    859.19 UE RA-RNTI 010b TC-RNTI deb5: initiating RA procedure
[NR_MAC]    Frame 859, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]    UE deb5: Msg3 scheduled at 860.17 (860.7 TDA 3) start 0 RBs 8
[NR_MAC]    UE deb5: 860.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 47, timing_offset = 0 (estimated distance 0.0 [m])
[NR_MAC]    860.7 Send RAR to RA-RNTI 010b
[NR_MAC]     860.17 PUSCH with TC_RNTI 0xdeb5 received correctly
[MAC]   [RAPROC] Received SDU for CCCH length 6 for UE deb5
[RLC]   Activated srb0 for UE 57013
[RLC]   Added srb 1 to UE 57013
[NR_MAC]    Activating scheduling Msg4 for TC_RNTI 0xdeb5 (state WAIT_Msg3)
[NR_RRC]    Decoding CCCH: RNTI deb5, payload_size 6
[NR_RRC]    [--] (cellID 0, UE ID 1 RNTI deb5) Create UE context: CU UE ID 1 DU UE ID 57013 (rnti: deb5, random ue id 52e00f5252000000)
[RRC]   activate SRB 1 of UE 1
[NR_RRC]    [DL] (cellID bc614e, UE ID 1 RNTI deb5) Send RRC Setup
[PHY]   [RAPROC] 860.19 prach_I0 = 21.6 dB
[NR_MAC]    UE deb5 Generate Msg4: feedback at  861.17, payload 225 bytes, next state nrRA_WAIT_Msg4_MsgB_ACK
[NR_MAC]    Adding new UE context with RNTI 0xdeb5
[NR_MAC]     861.17 UE deb5: Received Ack of Msg4. CBRA procedure succeeded!
[PHY]   [RAPROC] 861.19 prach_I0 = 21.1 dB
[PHY]   [RAPROC] 862.19 prach_I0 = 20.8 dB
[PHY]   [RAPROC] 863.19 prach_I0 = 20.5 dB
[NR_RRC]    [UL] (cellID bc614e, UE ID 1 RNTI deb5) Received RRCSetupComplete (RRC_CONNECTED reached)
[NGAP]    Selected PLMN in the NG Initial UE Message: MCC 1, MNC 1
[NGAP]    GUAMI in NGAP_NAS_FIRST_REQ (UE deb5): AMF Set ID 1016, Region ID 202, Pointer 0
[NGAP]    GUAMI is present: MCC=001 MNC=001 RegionID=202 SetID=1016 Pointer=0
[NGAP]    UE 1: Chose AMF 'AMF' (assoc_id 60) through GUAMI MCC 1 MNC 1 AMFRI 202 AMFSI 1016 AMFPT 0
[NGAP]    Create UE context (ID 1) for AMF 'AMF' (assoc_id 60)
[PHY]   [RAPROC] 864.19 prach_I0 = 20.2 dB
[NR_RRC]    [DL] (cellID bc614e, UE ID 1 RNTI deb5) Send DL Information Transfer [4 bytes]
[PHY]   [RAPROC] 865.19 prach_I0 = 19.8 dB
[PHY]   [RAPROC] 866.19 prach_I0 = 19.4 dB
[PHY]   [RAPROC] 867.19 prach_I0 = 20.2 dB
[NR_RRC]    [UL] (cellID bc614e, UE ID 1 RNTI deb5) Received RRC UL Information Transfer [28 bytes]
[PHY]   [RAPROC] 868.19 prach_I0 = 21.3 dB
[PHY]   [RAPROC] 869.19 prach_I0 = 20.9 dB
[PHY]   [RAPROC] 870.19 prach_I0 = 20.4 dB
[NR_RRC]    [DL] (cellID bc614e, UE ID 1 RNTI deb5) Send DL Information Transfer [42 bytes]
[PHY]   [RAPROC] 871.19 prach_I0 = 20.1 dB
[PHY]   [RAPROC] 872.19 prach_I0 = 19.6 dB
[PHY]   [RAPROC] 873.19 prach_I0 = 19.4 dB
[NR_RRC]    [UL] (cellID bc614e, UE ID 1 RNTI deb5) Received RRC UL Information Transfer [14 bytes]
[PHY]   [RAPROC] 874.19 prach_I0 = 19.1 dB
[NR_RRC]    [DL] (cellID bc614e, UE ID 1 RNTI deb5) Send DL Information Transfer [42 bytes]
[PHY]   [RAPROC] 875.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 876.19 prach_I0 = 18.8 dB
[PHY]   [RAPROC] 877.19 prach_I0 = 18.6 dB
[PHY]   [RAPROC] 878.19 prach_I0 = 18.4 dB
[PHY]   [RAPROC] 879.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 880.19 prach_I0 = 18.3 dB
[NR_RRC]    [UL] (cellID bc614e, UE ID 1 RNTI deb5) Received RRC UL Information Transfer [31 bytes]
[PHY]   [RAPROC] 881.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 882.19 prach_I0 = 17.9 dB
[NR_RRC]    [DL] (cellID bc614e, UE ID 1 RNTI deb5) Send DL Information Transfer [19 bytes]
[PHY]   [RAPROC] 883.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 884.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 885.19 prach_I0 = 18.8 dB
[NR_PHY]    [RAPROC] 886.19 Initiating RA procedure with preamble 6, energy 30.9 dB (I0 188, thres 120), delay 24 start symbol 0 freq index 0
[PHY]   [RAPROC] 886.19 prach_I0 = 20.2 dB
[NR_MAC]    886.19 UE RA-RNTI 010b TC-RNTI acaa: initiating RA procedure
[NR_MAC]    Frame 886, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]    UE acaa: Msg3 scheduled at 887.17 (887.7 TDA 3) start 0 RBs 8
[NR_MAC]    UE acaa: 887.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 6, timing_offset = 24 (estimated distance 937.5 [m])
[NR_MAC]    887.7 Send RAR to RA-RNTI 010b
[NR_RRC]    [UL] (cellID bc614e, UE ID 1 RNTI deb5) Received RRC UL Information Transfer [72 bytes]
[PHY]   [RAPROC] 887.19 prach_I0 = 20.9 dB
[NR_MAC]     88810: RA RNTI acaa CC_id 0 Scheduling retransmission of Msg3 in (888,17)
[PHY]   [RAPROC] 888.19 prach_I0 = 20.4 dB
[NR_MAC]     88910: RA RNTI acaa CC_id 0 Scheduling retransmission of Msg3 in (889,17)
[PHY]   [RAPROC] 889.19 prach_I0 = 20.0 dB
[NR_MAC]     89010: RA RNTI acaa CC_id 0 Scheduling retransmission of Msg3 in (890,17)
[NR_MAC]    UE acaa RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]    Remove NR rnti 0xacaa
[PHY]   [RAPROC] 890.19 prach_I0 = 19.6 dB
[NGAP]    NGAP_FIND_PROTOCOLIE_BY_ID ie is NULL (searching for ie: 110)
[NGAP]    NGAP_FIND_PROTOCOLIE_BY_ID ie is NULL (searching for ie: 71)
[NGAP]    AllowedNSSAI.list.count 1
[NR_RRC]    [--] (cellID bc614e, UE ID 1 RNTI deb5) Selected security algorithms: ciphering 0, integrity 2
[NR_RRC]    [UE deb5] Saved security key 19
[NR_RRC]    UE 1 Logical Channel DL-DCCH, Generate SecurityModeCommand (bytes 3)
[PHY]   [RAPROC] 891.19 prach_I0 = 19.4 dB
[PHY]   [RAPROC] 892.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 893.19 prach_I0 = 18.6 dB
[NR_RRC]    [UL] (cellID bc614e, UE ID 1 RNTI deb5) Received Security Mode Complete
[NR_RRC]    UE 1: Logical Channel DL-DCCH, Generate NR UECapabilityEnquiry (bytes 8, xid 3)
[PHY]   [RAPROC] 894.19 prach_I0 = 18.4 dB
[NR_MAC]    Frame.Slot 896.0
UE RNTI deb5 CU-UE-ID 1 in-sync PH 16 dB PCMAX 21 dBm, average RSRP -94 (4 meas)
UE deb5: dlsch_rounds 13/0/0/0, dlsch_errors 0, pucch0_DTX 0, BLER 0.07290 MCS (0) 0
UE deb5: ulsch_rounds 58/1/0/0, ulsch_errors 0, ulsch_DTX 1, BLER 0.07766 MCS (0) 0 (Qm 2 deltaMCS 0 dB) NPRB 5    SNR 44.5 dB
UE deb5: MAC:          TX            347 RX            719 bytes
UE deb5: LCID 1: TX            200 RX            363 bytes

[PHY]   [RAPROC] 895.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 896.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 897.19 prach_I0 = 18.8 dB
[PHY]   [RAPROC] 898.19 prach_I0 = 19.7 dB
[NR_RRC]    [UL] (cellID bc614e, UE ID 1 RNTI deb5) Received UE capabilities
[PHY]   [RAPROC] 899.19 prach_I0 = 20.2 dB
[NR_RRC]    Send message to ngap: NGAP_UE_CAPABILITIES_IND
[NR_RRC]    [DL] (cellID bc614e, UE ID 1 RNTI deb5) Send DL Information Transfer [51 bytes]
[NR_RRC]    Send message to sctp: NGAP_InitialContextSetupResponse
[PHY]   [RAPROC] 900.19 prach_I0 = 19.8 dB
[PHY]   [RAPROC] 901.19 prach_I0 = 19.5 dB
[NR_RRC]    [UL] (cellID bc614e, UE ID 1 RNTI deb5) Received RRC UL Information Transfer [13 bytes]
[PHY]   [RAPROC] 902.19 prach_I0 = 19.3 dB
[PHY]   [RAPROC] 903.19 prach_I0 = 19.1 dB
[PHY]   [RAPROC] 904.19 prach_I0 = 18.8 dB
[PHY]   [RAPROC] 905.19 prach_I0 = 18.6 dB
[PHY]   [RAPROC] 906.19 prach_I0 = 18.4 dB
[PHY]   [RAPROC] 907.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 908.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 909.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 910.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 911.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 912.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 913.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 914.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 915.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 916.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 917.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 918.19 prach_I0 = 17.6 dB
[PHY]   [RAPROC] 919.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 920.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 921.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 922.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 923.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 924.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 925.19 prach_I0 = 17.4 dB
[NR_RRC]    [UL] (cellID bc614e, UE ID 1 RNTI deb5) Received RRC UL Information Transfer [81 bytes]
[PHY]   [RAPROC] 926.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 927.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 928.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 929.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 930.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 931.19 prach_I0 = 17.3 dB
[NGAP]    PDUSESSIONSetup initiating message
[NR_RRC]    UE 1: received PDU Session Resource Setup Request
[NR_RRC]    Adding pdusession 11, total nb of sessions 1
[NR_RRC]    UE 1: configure DRB ID 1 for PDU session ID 11
[NR_RRC]    [--] (cellID bc614e, UE ID 1 RNTI deb5) second best match: CU-UP ID 3584 matches SST 1
[RRC]   UE 1 associating to CU-UP assoc_id -1 out of 1 CU-UPs
[E1AP]    UE 1: add PDU session ID 11 (1 bearers)
[GTPU]    [94] Created tunnel for UE ID 1, teid for incoming: 3a2b8033, teid for outgoing 4f to remote IPv4: 192.168.8.21, IPv6 ::
[PDCP]    added drb 1 to UE ID 1
[SDAP]    Default DRB for the created SDAP entity: 1
[RRC]   activate SRB 2 of UE 1
[PHY]   [RAPROC] 932.19 prach_I0 = 17.4 dB
[RLC]   Added srb 2 to UE 57013
[RLC]   Added drb 1 to UE 57013
[RLC]   Added DRB to UE 57013
[NR_RRC]    SRS configured with 1 ports
[RRC]   UE 1 trigger UE context setup request with 1 DRBs
[RRC]   UE deb5 replacing existing CellGroupConfig with new one received from DU
[E1AP]    UE 1: updating PDU session ID 11 (1 bearers)
[PDCP]    DRB 1 re-established
[NR_RRC]    [DL] (cellID bc614e, UE ID 1 RNTI deb5) Generate RRCReconfiguration (bytes 327, xid 1)
[RRC]   UE 1: PDU session ID 11 modified 1 bearers
[PHY]   [RAPROC] 933.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 934.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 935.19 prach_I0 = 18.0 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 936.19 prach_I0 = 17.9 dB
[NR_RRC]    [UL] (cellID bc614e, UE ID 1 RNTI deb5) Received RRCReconfigurationComplete
[NR_RRC]    msg index 0, pdu_sessions index 0, status 2, xid 1): nb_of_pdusessions 1,  pdusession_id 11, teid: 975929395
 [NR_RRC]    NGAP_PDUSESSION_SETUP_RESP: sending the message
[NGAP]    pdusession_setup_resp_p: pdusession ID 11, gnb_addr 192.168.70.129, SIZE 4, TEID 975929395
[NR_MAC]    DU received confirmation of successful RRC Reconfiguration
[PHY]   [RAPROC] 937.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 938.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 939.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 940.19 prach_I0 = 17.8 dB
[PHY]   [RAPROC] 941.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 942.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 943.19 prach_I0 = 17.5 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 944.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 945.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 946.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 947.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 948.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 949.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 950.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 951.19 prach_I0 = 17.3 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 952.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 953.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 954.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 955.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 956.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 957.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 958.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 959.19 prach_I0 = 17.4 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 960.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 961.19 prach_I0 = 17.0 dB
[PHY]   [RAPROC] 962.19 prach_I0 = 17.0 dB
[PHY]   [RAPROC] 963.19 prach_I0 = 17.0 dB
[PHY]   [RAPROC] 964.19 prach_I0 = 16.9 dB
[PHY]   [RAPROC] 965.19 prach_I0 = 16.9 dB
[PHY]   [RAPROC] 966.19 prach_I0 = 16.8 dB
[PHY]   [RAPROC] 967.19 prach_I0 = 16.8 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 968.19 prach_I0 = 16.8 dB
[PHY]   [RAPROC] 969.19 prach_I0 = 16.9 dB
[PHY]   [RAPROC] 970.19 prach_I0 = 16.8 dB
[PHY]   [RAPROC] 971.19 prach_I0 = 16.8 dB
[PHY]   [RAPROC] 972.19 prach_I0 = 16.9 dB
[PHY]   [RAPROC] 973.19 prach_I0 = 16.8 dB
[PHY]   [RAPROC] 974.19 prach_I0 = 16.8 dB
[PHY]   [RAPROC] 975.19 prach_I0 = 16.9 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 976.19 prach_I0 = 17.0 dB
[PHY]   [RAPROC] 977.19 prach_I0 = 17.0 dB
[PHY]   [RAPROC] 978.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 979.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 980.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 981.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 982.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 983.19 prach_I0 = 17.5 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 984.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 985.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 986.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 987.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 988.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 989.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 990.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 991.19 prach_I0 = 17.2 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 992.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 993.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 994.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 995.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 996.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 997.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 998.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 999.19 prach_I0 = 17.2 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 1000.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 1001.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 1002.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 1003.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 1004.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 1005.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 1006.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 1007.19 prach_I0 = 17.2 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 1008.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 1009.19 prach_I0 = 17.1 dB
[PHY]   [RAPROC] 1010.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 1011.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 1012.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 1013.19 prach_I0 = 17.2 dB
[PHY]   [RAPROC] 1014.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 1015.19 prach_I0 = 17.8 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
[PHY]   [RAPROC] 1016.19 prach_I0 = 17.7 dB
[PHY]   [RAPROC] 1017.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 1018.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 1019.19 prach_I0 = 17.5 dB
[PHY]   [RAPROC] 1020.19 prach_I0 = 17.4 dB
[PHY]   [RAPROC] 1021.19 prach_I0 = 17.3 dB
[PHY]   [RAPROC] 1022.19 prach_I0 = 17.4 dB
[NR_MAC]    Frame.Slot 0.0
UE RNTI deb5 CU-UE-ID 1 in-sync PH 42 dB PCMAX 21 dBm, average RSRP -93 (16 meas)
UE deb5: dlsch_rounds 22/0/0/0, dlsch_errors 0, pucch0_DTX 0, BLER 0.04783 MCS (1) 0
UE deb5: ulsch_rounds 108/2/0/0, ulsch_errors 0, ulsch_DTX 2, BLER 0.03234 MCS (1) 0 (Qm 2 deltaMCS 0 dB) NPRB 5    SNR 19.5 dB
UE deb5: MAC:          TX            884 RX           2830 bytes
UE deb5: LCID 1: TX            617 RX           1540 bytes
UE deb5: LCID 2: TX              0 RX              0 bytes
UE deb5: LCID 4: TX              3 RX            219 bytes

[PHY]   [RAPROC] 1023.19 prach_I0 = 17.3 dB
[NR_MAC]    Invalid timing advance offset for RNTI deb5
"""

frames = []
prach_i0_values = []

# Regex to find lines with "prach_I0 = X.Y dB"
# It captures the number before ".19" as the frame and X.Y as prach_I0 value
# This regex also handles the specific line "PHY] prach_I0 = 17.3 dB" which lacks a frame number
pattern = re.compile(r'(?:\[PHY\]\s+\[RAPROC\]\s+)?(\d+\.\d+)\s+prach_I0\s*=\s*(\d+\.\d+)\s*dB')
fallback_pattern = re.compile(r'\[PHY\]\s+prach_I0\s*=\s*(\d+\.\d+)\s*dB')

for line in log_data.strip().split('\n'):
    match = pattern.search(line)
    if match:
        frame_full = match.group(1)
        # Extract just the integer part as the frame number
        frame = int(float(frame_full))
        prach_i0 = float(match.group(2))
        frames.append(frame)
        prach_i0_values.append(prach_i0)
    else:
        # Handle the specific case where the frame number is missing
        fallback_match = fallback_pattern.search(line)
        if fallback_match:
            # For these cases, we might need to infer the frame or handle it differently.
            # For now, let's skip it or assign a placeholder/previous frame if logical.
            # Given the request is for "each frame", skipping is safer if no explicit frame.
            # If you want to associate these with the previous frame, you'd need to modify this logic.
            # For this example, we'll skip lines that don't have the frame.xx format before prach_I0
            pass

# Create the plot with analysis
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

# 主要時間序列圖
ax1.plot(frames, prach_i0_values, marker='o', linestyle='-', color='b', markersize=3)
ax1.set_title('prach_I0 隨 Frame 的變化 (時間序列)', fontsize=14)
ax1.set_xlabel('Frame')
ax1.set_ylabel('prach_I0 (dB)')
ax1.grid(True, alpha=0.3)

# 添加統計線
mean_val = np.mean(prach_i0_values)
std_val = np.std(prach_i0_values)
ax1.axhline(y=mean_val, color='r', linestyle='--', alpha=0.8, label=f'平均值: {mean_val:.2f} dB')
ax1.axhline(y=mean_val + std_val, color='orange', linestyle=':', alpha=0.8, label=f'+1σ: {mean_val + std_val:.2f} dB')
ax1.axhline(y=mean_val - std_val, color='orange', linestyle=':', alpha=0.8, label=f'-1σ: {mean_val - std_val:.2f} dB')
ax1.legend()

# 直方圖分析
ax2.hist(prach_i0_values, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
ax2.axvline(mean_val, color='r', linestyle='--', linewidth=2, label=f'平均值: {mean_val:.2f} dB')
ax2.axvline(np.median(prach_i0_values), color='g', linestyle='--', linewidth=2, label=f'中位數: {np.median(prach_i0_values):.2f} dB')
ax2.set_title('prach_I0 數值分布直方圖', fontsize=14)
ax2.set_xlabel('prach_I0 (dB)')
ax2.set_ylabel('頻次')
ax2.legend()
ax2.grid(True, alpha=0.3)

# 移動平均分析
window_size = 20
if len(prach_i0_values) >= window_size:
    moving_avg = np.convolve(prach_i0_values, np.ones(window_size)/window_size, mode='valid')
    moving_frames = frames[window_size-1:]
    ax3.plot(frames, prach_i0_values, alpha=0.3, color='lightblue', label='原始數據')
    ax3.plot(moving_frames, moving_avg, color='red', linewidth=2, label=f'{window_size}點移動平均')
    ax3.set_title(f'prach_I0 移動平均分析 (窗口大小: {window_size})', fontsize=14)
    ax3.set_xlabel('Frame')
    ax3.set_ylabel('prach_I0 (dB)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

# 數據變化率分析
changes = np.diff(prach_i0_values)
change_frames = frames[1:]
ax4.plot(change_frames, changes, marker='o', linestyle='-', color='purple', markersize=2)
ax4.axhline(y=0, color='black', linestyle='-', alpha=0.5)
ax4.set_title('prach_I0 變化率分析 (相鄰Frame差值)', fontsize=14)
ax4.set_xlabel('Frame')
ax4.set_ylabel('prach_I0 變化量 (dB)')
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 詳細統計分析
print("="*60)
print("prach_I0 數據統計分析報告")
print("="*60)

print(f"\n【基本統計資訊】")
print(f"數據點總數: {len(prach_i0_values)}")
print(f"Frame 範圍: {min(frames)} ~ {max(frames)}")
print(f"prach_I0 範圍: {min(prach_i0_values):.1f} ~ {max(prach_i0_values):.1f} dB")
print(f"平均值: {mean_val:.2f} dB")
print(f"中位數: {np.median(prach_i0_values):.2f} dB")
print(f"標準差: {std_val:.2f} dB")
print(f"變異係數: {(std_val/mean_val)*100:.1f}%")

print(f"\n【分位數分析】")
percentiles = [5, 10, 25, 50, 75, 90, 95]
for p in percentiles:
    val = np.percentile(prach_i0_values, p)
    print(f"{p}% 分位數: {val:.2f} dB")

print(f"\n【異常值檢測】(使用 IQR 方法)")
Q1 = np.percentile(prach_i0_values, 25)
Q3 = np.percentile(prach_i0_values, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = [val for val in prach_i0_values if val < lower_bound or val > upper_bound]
print(f"IQR: {IQR:.2f} dB")
print(f"異常值範圍: < {lower_bound:.2f} dB 或 > {upper_bound:.2f} dB")
print(f"異常值數量: {len(outliers)} 個")
if outliers:
    print(f"異常值: {sorted(set(outliers))}")

print(f"\n【數據穩定性分析】")
print(f"最大變化量: {max(abs(change) for change in changes):.2f} dB")
print(f"平均變化量: {np.mean(np.abs(changes)):.2f} dB")
print(f"變化量標準差: {np.std(changes):.2f} dB")

print(f"\n【關鍵事件識別】")
# 尋找大幅變化的點
large_changes = [(i+1, change) for i, change in enumerate(changes) if abs(change) > 2*np.std(changes)]
if large_changes:
    print("大幅變化事件 (變化量 > 2σ):")
    for frame_idx, change in large_changes[:10]:  # 顯示前10個
        frame_num = frames[frame_idx]
        val_before = prach_i0_values[frame_idx-1]
        val_after = prach_i0_values[frame_idx]
        print(f"  Frame {frame_num}: {val_before:.1f} → {val_after:.1f} dB (變化: {change:+.1f} dB)")

# 尋找最高和最低值
max_idx = prach_i0_values.index(max(prach_i0_values))
min_idx = prach_i0_values.index(min(prach_i0_values))
print(f"\n最高值: {max(prach_i0_values):.1f} dB (Frame {frames[max_idx]})")
print(f"最低值: {min(prach_i0_values):.1f} dB (Frame {frames[min_idx]})")

print(f"\n【趨勢分析】")
# 簡單線性回歸
x = np.array(range(len(prach_i0_values)))
y = np.array(prach_i0_values)
slope, intercept = np.polyfit(x, y, 1)
print(f"整體趨勢斜率: {slope:.4f} dB/點")
if abs(slope) < 0.001:
    trend = "基本穩定"
elif slope > 0:
    trend = "略微上升"
else:
    trend = "略微下降"
print(f"趨勢判定: {trend}")

print("="*60)

print("已提取的 Frame 和 prach_I0 數據：")
for i in range(len(frames)):
    print(f"Frame: {frames[i]}, prach_I0: {prach_i0_values[i]} dB")