實際上 get_cce_index 不計數 free CCE 的數量，它只做二元判斷：「能不能找到一個 aggregation_level × candidate 個 CCE 的連續區塊是空的？」

若要知道同一 slot 中有多少 CCE 已被佔用，需要看 vrb_map 的狀態 — 由先前已排程的 PDCCH（如其他 UE 的 DCI、SIB1、Paging 等）透過 fill_pdcch_vrb_map (gNB_scheduler_primitives.c:591) 寫入。

結論
影響 Free CCE 的因素	說明
CORESET 大小 (N_rb × duration / 6)	決定上限
同 slot 內已排程的其他 PDCCH	透過 vrb_map 佔用 REG
Aggregation level	越大越容易找不到（需要更多連續 CCE）
is_common = true → Y=0	candidate 位置固定，不隨 RNTI 散亂
Msg2 用 pdcch_cl_adjust = 0，因此優先嘗試最小的 aggregation level（L=1），能最大化找到空閒 candidate 的機會。若 CORESET 資源已被其他 PDCCH 耗盡，才會回傳 -1。