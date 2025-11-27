# Zotero Database Schema

## Table: `fieldFormats`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| fieldFormatID | INTEGER | False | None | True |
| regex | TEXT | False | None | False |
| isInteger | INT | False | None | False |

### Sample Data (first 5 rows)

| fieldFormatID | regex | isInteger |
|---|---|---|
| 1 | .* | 0 |
| 2 | [0-9]* | 1 |
| 3 | [0-9]{4} | 1 |

## Table: `charsets`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| charsetID | INTEGER | False | None | True |
| charset | TEXT | False | None | False |

### Sample Data (first 5 rows)

| charsetID | charset |
|---|---|
| 1 | utf-8 |
| 2 | big5 |
| 3 | euc-jp |
| 4 | euc-kr |
| 5 | gb18030 |

## Table: `fileTypes`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| fileTypeID | INTEGER | False | None | True |
| fileType | TEXT | False | None | False |

### Sample Data (first 5 rows)

| fileTypeID | fileType |
|---|---|
| 1 | webpage |
| 2 | image |
| 3 | pdf |
| 4 | audio |
| 5 | video |

## Table: `fileTypeMimeTypes`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| fileTypeID | INT | False | None | True |
| mimeType | TEXT | False | None | True |

### Sample Data (first 5 rows)

| fileTypeID | mimeType |
|---|---|
| 1 | text/html |
| 2 | image/ |
| 2 | application/vnd.oasis.opendocument.graphics |
| 2 | application/vnd.oasis.opendocument.image |
| 3 | application/pdf |

## Table: `syncObjectTypes`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| syncObjectTypeID | INTEGER | False | None | True |
| name | TEXT | False | None | False |

### Sample Data (first 5 rows)

| syncObjectTypeID | name |
|---|---|
| 1 | collection |
| 2 | creator |
| 3 | item |
| 4 | search |
| 5 | tag |

## Table: `itemTypes`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemTypeID | INTEGER | False | None | True |
| typeName | TEXT | False | None | False |
| templateItemTypeID | INT | False | None | False |
| display | INT | False | 1 | False |

### Sample Data (first 5 rows)

| itemTypeID | typeName | templateItemTypeID | display |
|---|---|---|---|
| 1 | annotation | None | 1 |
| 2 | artwork | None | 1 |
| 3 | attachment | None | 1 |
| 4 | audioRecording | None | 1 |
| 5 | bill | None | 1 |

## Table: `itemTypesCombined`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemTypeID | INT | True | None | True |
| typeName | TEXT | True | None | False |
| display | INT | True | 1 | False |
| custom | INT | True | None | False |

### Sample Data (first 5 rows)

| itemTypeID | typeName | display | custom |
|---|---|---|---|
| 1 | annotation | 1 | 0 |
| 2 | artwork | 1 | 0 |
| 3 | attachment | 1 | 0 |
| 4 | audioRecording | 1 | 0 |
| 5 | bill | 1 | 0 |

## Table: `fields`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| fieldID | INTEGER | False | None | True |
| fieldName | TEXT | False | None | False |
| fieldFormatID | INT | False | None | False |

### Sample Data (first 5 rows)

| fieldID | fieldName | fieldFormatID |
|---|---|---|
| 1 | title | None |
| 2 | abstractNote | None |
| 3 | artworkMedium | None |
| 4 | medium | None |
| 5 | artworkSize | None |

## Table: `fieldsCombined`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| fieldID | INT | True | None | True |
| fieldName | TEXT | True | None | False |
| label | TEXT | False | None | False |
| fieldFormatID | INT | False | None | False |
| custom | INT | True | None | False |

### Sample Data (first 5 rows)

| fieldID | fieldName | label | fieldFormatID | custom |
|---|---|---|---|---|
| 1 | title | None | None | 0 |
| 2 | abstractNote | None | None | 0 |
| 3 | artworkMedium | None | None | 0 |
| 4 | medium | None | None | 0 |
| 5 | artworkSize | None | None | 0 |

## Table: `itemTypeFields`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemTypeID | INT | False | None | True |
| fieldID | INT | False | None | False |
| hide | INT | False | None | False |
| orderIndex | INT | False | None | True |

### Sample Data (first 5 rows)

| itemTypeID | fieldID | hide | orderIndex |
|---|---|---|---|
| 2 | 1 | 0 | 0 |
| 2 | 2 | 0 | 1 |
| 2 | 3 | 0 | 2 |
| 2 | 5 | 0 | 3 |
| 2 | 6 | 0 | 4 |

## Table: `itemTypeFieldsCombined`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemTypeID | INT | True | None | True |
| fieldID | INT | True | None | False |
| hide | INT | False | None | False |
| orderIndex | INT | True | None | True |

### Sample Data (first 5 rows)

| itemTypeID | fieldID | hide | orderIndex |
|---|---|---|---|
| 2 | 1 | 0 | 0 |
| 2 | 2 | 0 | 1 |
| 2 | 3 | 0 | 2 |
| 2 | 5 | 0 | 3 |
| 2 | 6 | 0 | 4 |

## Table: `baseFieldMappings`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemTypeID | INT | False | None | True |
| baseFieldID | INT | False | None | True |
| fieldID | INT | False | None | True |

### Sample Data (first 5 rows)

| itemTypeID | baseFieldID | fieldID |
|---|---|---|
| 2 | 4 | 3 |
| 4 | 4 | 17 |
| 4 | 23 | 22 |
| 5 | 27 | 26 |
| 5 | 19 | 29 |

## Table: `baseFieldMappingsCombined`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemTypeID | INT | False | None | True |
| baseFieldID | INT | False | None | True |
| fieldID | INT | False | None | True |

### Sample Data (first 5 rows)

| itemTypeID | baseFieldID | fieldID |
|---|---|---|
| 2 | 4 | 3 |
| 4 | 4 | 17 |
| 4 | 23 | 22 |
| 5 | 19 | 29 |
| 5 | 27 | 26 |

## Table: `creatorTypes`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| creatorTypeID | INTEGER | False | None | True |
| creatorType | TEXT | False | None | False |

### Sample Data (first 5 rows)

| creatorTypeID | creatorType |
|---|---|
| 1 | artist |
| 2 | contributor |
| 3 | performer |
| 4 | composer |
| 5 | wordsBy |

## Table: `itemTypeCreatorTypes`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemTypeID | INT | False | None | True |
| creatorTypeID | INT | False | None | True |
| primaryField | INT | False | None | False |

### Sample Data (first 5 rows)

| itemTypeID | creatorTypeID | primaryField |
|---|---|---|
| 2 | 1 | 1 |
| 2 | 2 | 0 |
| 4 | 3 | 1 |
| 4 | 2 | 0 |
| 4 | 4 | 0 |

## Table: `version`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| schema | TEXT | False | None | True |
| version | INT | True | None | False |

### Sample Data (first 5 rows)

| schema | version |
|---|---|
| globalSchema | 33 |
| system | 32 |
| userdata | 123 |
| triggers | 18 |
| compatibility | 7 |

## Table: `settings`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| setting | TEXT | False | None | True |
| key | TEXT | False | None | True |
| value |  | False | None | False |

### Sample Data (first 5 rows)

| setting | key | value |
|---|---|---|
| globalSchema | data | b"x\x9c\xec\xbd\xdbs\x1dE\x9a\xe8\xfb\xafT\xe4<tw\x84\x85\x1f\xf6\x1b/'d[\x80\xf1\x05\x1dK\x98=\xec\xd81Q\xd2*I\xe5\xb5\xb4jM]\x84\xad\x1d\x13\xd1666\x04=\xd3t\xc344\xdd\r\xa6\xdd\xf8\xb21F\xbea\x9b\x8b#f\xc1\xab,^\xb6%\xe6m\xff%\xe7\xbb\xe4=\xb3\xd6Z2\x9e\xd9\xfbD\x10\x84Q"... [truncated] |
| client | lastCompatibleVersion | 7.0.29 |
| account | localUserKey | q6gIGVbQ |
| account | username | AlexKulibaba |
| account | userID | 14445519 |

## Table: `syncedSettings`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| setting | TEXT | True | None | True |
| libraryID | INT | True | None | True |
| value |  | True | None | False |
| version | INT | True | 0 | False |
| synced | INT | True | 0 | False |

### Sample Data (first 5 rows)

| setting | libraryID | value | version | synced |
|---|---|---|---|---|
| lastPageIndex_u_A9YQUV6D | 1 | 0 | 711 | 1 |
| lastPageIndex_u_NFQLZPI7 | 1 | 0 | 843 | 1 |
| lastPageIndex_g5560629_3KXHDYNX | 1 | 0 | 615 | 1 |
| lastPageIndex_g5560629_4RPBNXD9 | 1 | 0 | 91 | 1 |
| lastPageIndex_g5560629_5AF2Q38G | 1 | 0 | 820 | 1 |

## Table: `items`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INTEGER | False | None | True |
| itemTypeID | INT | True | None | False |
| dateAdded | TIMESTAMP | True | CURRENT_TIMESTAMP | False |
| dateModified | TIMESTAMP | True | CURRENT_TIMESTAMP | False |
| clientDateModified | TIMESTAMP | True | CURRENT_TIMESTAMP | False |
| libraryID | INT | True | None | False |
| key | TEXT | True | None | False |
| version | INT | True | 0 | False |
| synced | INT | True | 0 | False |

### Sample Data (first 5 rows)

| itemID | itemTypeID | dateAdded | dateModified | clientDateModified | libraryID | key | version | synced |
|---|---|---|---|---|---|---|---|---|
| 1 | 11 | 2025-10-30 16:47:31 | 2025-10-30 16:47:31 | 2025-10-30 16:47:31 | 1 | GSMJ7JRK | 712 | 1 |
| 2 | 3 | 2025-10-30 16:47:32 | 2025-10-30 16:47:32 | 2025-10-30 16:47:32 | 1 | LNQJ6VUM | 720 | 1 |
| 3 | 11 | 2025-10-30 17:30:48 | 2025-10-30 17:30:48 | 2025-10-30 17:30:48 | 1 | STGJGZPZ | 712 | 1 |
| 4 | 28 | 2025-10-30 17:30:48 | 2025-10-30 17:30:48 | 2025-10-30 17:30:48 | 1 | F253AUC5 | 712 | 1 |
| 5 | 3 | 2025-10-30 17:30:50 | 2025-10-30 17:30:50 | 2025-10-30 17:30:50 | 1 | JCKN2APG | 716 | 1 |

## Table: `itemDataValues`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| valueID | INTEGER | False | None | True |
| value |  | False | None | False |

### Sample Data (first 5 rows)

| valueID | value |
|---|---|
| 1 | Aspirations and Practice of ML Model Documentation: Moving the Needle with Nudging and Traceability |
| 2 | The documentation practice for machine-learned (ML) models often falls short of established practice... [truncated] |
| 3 | 2023-04-19 April 19, 2023 |
| 4 | Aspirations and Practice of ML Model Documentation |
| 5 | ACM Digital Library |

## Table: `itemData`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INT | False | None | True |
| fieldID | INT | False | None | True |
| valueID |  | False | None | False |

### Sample Data (first 5 rows)

| itemID | fieldID | valueID |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 2 | 2 |
| 1 | 6 | 3 |
| 1 | 8 | 4 |
| 1 | 11 | 5 |

## Table: `itemNotes`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INTEGER | False | None | True |
| parentItemID | INT | False | None | False |
| note | TEXT | False | None | False |
| title | TEXT | False | None | False |

### Sample Data (first 5 rows)

| itemID | parentItemID | note | title |
|---|---|---|---|
| 4 | 3 | <div class="zotero-note znv1">Comment: To appear at ACM FAccT'22</div> | Comment: To appear at ACM FAccT'22 |
| 11 | 10 | <div class="zotero-note znv1">Comment: Camera-ready preprint of paper accepted to CSCW 2022</div> | Comment: Camera-ready preprint of paper accepted to CSCW 2022 |
| 110 | 59 | <div class="zotero-note znv1">Comment: Working in progress</div> | Comment: Working in progress |
| 117 | 63 | <div class="zotero-note znv1">Comment: 9 pages, 7 figures, accepted to the main conference of ACL 20... [truncated] | Comment: 9 pages, 7 figures, accepted to the main conference of ACL 2023 |
| 120 | 64 | <div class="zotero-note znv1">Comment: To appear in LREC-COLING 2024, short paper (preprint)</div> | Comment: To appear in LREC-COLING 2024, short paper (preprint) |

## Table: `itemAttachments`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INTEGER | False | None | True |
| parentItemID | INT | False | None | False |
| linkMode | INT | False | None | False |
| contentType | TEXT | False | None | False |
| charsetID | INT | False | None | False |
| path | TEXT | False | None | False |
| syncState | INT | False | 0 | False |
| storageModTime | INT | False | None | False |
| storageHash | TEXT | False | None | False |
| lastProcessedModificationTime | INT | False | None | False |

### Sample Data (first 5 rows)

| itemID | parentItemID | linkMode | contentType | charsetID | path | syncState | storageModTime | storageHash | lastProcessedModificationTime |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 1 | 1 | application/pdf | None | storage:Bhat et al. - 2023 - Aspirations and Practice of ML Model Documentation Moving the Needle wi... [truncated] | 2 | 1761842852442 | a9630b7db68ed43d545a688a05002e4e | None |
| 5 | 3 | 1 | application/pdf | None | storage:Crisan et al. - 2022 - Interactive Model Cards A Human-Centered Approach to Model Documentat... [truncated] | 2 | 1761845450539 | 7cece282cd464239d07ba91a257fe50d | None |
| 6 | 3 | 1 | text/html | 1 | storage:2205.html | 2 | 1761845452958 | 4d8a9e52a69fb9802f4fe315f5628500 | None |
| 8 | 7 | 1 | application/pdf | None | storage:Mitchell et al. - 2019 - Model Cards for Model Reporting.pdf | 2 | 1761845513539 | cdc53c1602d8d4e8ba9691465d518d8e | None |
| 9 | 7 | 1 | text/html | 1 | storage:1810.html | 2 | 1761845516884 | 29efa2d2571bb6fa400716337c1ff920 | None |

## Table: `itemAnnotations`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INTEGER | False | None | True |
| parentItemID | INT | True | None | False |
| type | INTEGER | True | None | False |
| authorName | TEXT | False | None | False |
| text | TEXT | False | None | False |
| comment | TEXT | False | None | False |
| color | TEXT | False | None | False |
| pageLabel | TEXT | False | None | False |
| sortIndex | TEXT | True | None | False |
| position | TEXT | True | None | False |
| isExternal | INT | True | None | False |

### Sample Data (first 5 rows)

| itemID | parentItemID | type | authorName | text | comment | color | pageLabel | sortIndex | position | isExternal |
|---|---|---|---|---|---|---|---|---|---|---|
| 16 | 12 | 1 | None | Participants expressed needs for data documentation frameworks to be adaptable to their contexts, in... [truncated] | None | #ffd400 | 1 | 00000\|001340\|00337 | {"pageIndex":0,"rects":[[193.32,373.586,440.239,382.319],[45.84,362.546,440.016,371.28],[45.84,351.6... [truncated] | 0 |
| 174 | 99 | 1 | None | sequenceto-sequence framework. | None | #ffd400 | 1 | 00000\|000273\|00272 | {"pageIndex":0,"rects":[[233.426,560.866,273.256,569.773],[89.008,548.911,185.864,557.818]]} | 0 |
| 179 | 101 | 1 | None | both zero-shot and fewshot prompting, as well as human evaluations of the results. These studies bot... [truncated] | None | #ffd400 | 2 | 00001\|002366\|00239 | {"pageIndex":1,"rects":[[418.156,592.721,526.224,602.473],[306.142,579.172,524.408,588.924],[306.142... [truncated] | 0 |
| 180 | 101 | 1 | None | he previous studies on ChatGPT ask participants to identify phenomena such as overcorrections and un... [truncated] | None | #ffd400 | 2 | 00001\|002683\|00349 | {"pageIndex":1,"rects":[[354.334,483.129,524.682,492.881],[306.142,469.58,526.217,479.332],[306.142,... [truncated] | 0 |
| 185 | 125 | 1 | None | me that an error can be corrected in four ways: insert, delete, replace, and relocate | None | #ffd400 | 2 | 00001\|002819\|00358 | {"pageIndex":1,"rects":[[401.314,473.413,526.217,483.165],[306.142,459.864,524.415,469.616],[306.142... [truncated] | 0 |

## Table: `tags`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| tagID | INTEGER | False | None | True |
| name | TEXT | True | None | False |

### Sample Data (first 5 rows)

| tagID | name |
|---|---|
| 1 | Computer Science - Artificial Intelligence |
| 2 | Computer Science - Computation and Language |
| 3 | Computer Science - Human-Computer Interaction |
| 4 | Computer Science - Machine Learning |
| 5 | Documentation Requirements |

## Table: `itemRelations`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INT | True | None | True |
| predicateID | INT | True | None | True |
| object | TEXT | True | None | True |

### Sample Data (first 5 rows)

| itemID | predicateID | object |
|---|---|---|
| 10 | 1 | http://zotero.org/groups/6265004/items/2557R4F9 |
| 11 | 1 | http://zotero.org/groups/6265004/items/RQDXCQFU |
| 12 | 1 | http://zotero.org/groups/6265004/items/6B9LQJWD |
| 13 | 1 | http://zotero.org/groups/6265004/items/QD5WQIR7 |
| 984 | 1 | http://zotero.org/groups/6265004/items/QM92ZMNJ |

## Table: `itemTags`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INT | True | None | True |
| tagID | INT | True | None | True |
| type | INT | True | None | False |

### Sample Data (first 5 rows)

| itemID | tagID | type |
|---|---|---|
| 3 | 1 | 1 |
| 3 | 2 | 1 |
| 3 | 3 | 1 |
| 7 | 1 | 1 |
| 7 | 4 | 1 |

## Table: `creators`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| creatorID | INTEGER | False | None | True |
| firstName | TEXT | False | None | False |
| lastName | TEXT | False | None | False |
| fieldMode | INT | False | None | False |

### Sample Data (first 5 rows)

| creatorID | firstName | lastName | fieldMode |
|---|---|---|---|
| 1 | Avinash | Bhat | 0 |
| 2 | Austin | Coursey | 0 |
| 3 | Grace | Hu | 0 |
| 4 | Sixian | Li | 0 |
| 5 | Nadia | Nahar | 0 |

## Table: `itemCreators`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INT | True | None | True |
| creatorID | INT | True | None | True |
| creatorTypeID | INT | True | 1 | True |
| orderIndex | INT | True | 0 | True |

### Sample Data (first 5 rows)

| itemID | creatorID | creatorTypeID | orderIndex |
|---|---|---|---|
| 1 | 1 | 8 | 0 |
| 1 | 2 | 8 | 1 |
| 1 | 3 | 8 | 2 |
| 1 | 4 | 8 | 3 |
| 1 | 5 | 8 | 4 |

## Table: `collections`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| collectionID | INTEGER | False | None | True |
| collectionName | TEXT | True | None | False |
| parentCollectionID | INT | False | NULL | False |
| clientDateModified | TIMESTAMP | True | CURRENT_TIMESTAMP | False |
| libraryID | INT | True | None | False |
| key | TEXT | True | None | False |
| version | INT | True | 0 | False |
| synced | INT | True | 0 | False |

### Sample Data (first 5 rows)

| collectionID | collectionName | parentCollectionID | clientDateModified | libraryID | key | version | synced |
|---|---|---|---|---|---|---|---|
| 1 | SOTA for GEC | None | 2025-11-02 12:49:17 | 2 | UHU46U77 | 141 | 1 |
| 2 | GEC using LLM's | None | 2025-11-02 12:49:17 | 2 | 9PKS93TK | 138 | 1 |
| 3 | Active Learning / Explorables | None | 2025-11-02 12:49:17 | 2 | CISVX9DU | 130 | 1 |
| 4 | Datasheets | None | 2025-11-02 12:52:21 | 3 | UUCS97FQ | 10 | 1 |
| 5 | Model Cards | None | 2025-11-02 12:52:21 | 3 | KSQK5J6C | 8 | 1 |

## Table: `collectionItems`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| collectionID | INT | True | None | True |
| itemID | INT | True | None | True |
| orderIndex | INT | True | 0 | False |

### Sample Data (first 5 rows)

| collectionID | itemID | orderIndex |
|---|---|---|
| 1 | 37 | 0 |
| 2 | 38 | 0 |
| 2 | 41 | 1 |
| 2 | 42 | 2 |
| 2 | 43 | 3 |

## Table: `collectionRelations`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| collectionID | INT | True | None | True |
| predicateID | INT | True | None | True |
| object | TEXT | True | None | True |

### Sample Data (first 5 rows)

No data in this table.

## Table: `feeds`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| libraryID | INTEGER | False | None | True |
| name | TEXT | True | None | False |
| url | TEXT | True | None | False |
| lastUpdate | TIMESTAMP | False | None | False |
| lastCheck | TIMESTAMP | False | None | False |
| lastCheckError | TEXT | False | None | False |
| cleanupReadAfter | INT | False | None | False |
| cleanupUnreadAfter | INT | False | None | False |
| refreshInterval | INT | False | None | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `feedItems`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INTEGER | False | None | True |
| guid | TEXT | True | None | False |
| readTime | TIMESTAMP | False | None | False |
| translatedTime | TIMESTAMP | False | None | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `savedSearches`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| savedSearchID | INTEGER | False | None | True |
| savedSearchName | TEXT | True | None | False |
| clientDateModified | TIMESTAMP | True | CURRENT_TIMESTAMP | False |
| libraryID | INT | True | None | False |
| key | TEXT | True | None | False |
| version | INT | True | 0 | False |
| synced | INT | True | 0 | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `savedSearchConditions`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| savedSearchID | INT | True | None | True |
| searchConditionID | INT | True | None | True |
| condition | TEXT | True | None | False |
| operator | TEXT | False | None | False |
| value | TEXT | False | None | False |
| required | NONE | False | None | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `deletedCollections`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| collectionID | INTEGER | False | None | True |
| dateDeleted |  | True | CURRENT_TIMESTAMP | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `deletedItems`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INTEGER | False | None | True |
| dateDeleted |  | True | CURRENT_TIMESTAMP | False |

### Sample Data (first 5 rows)

| itemID | dateDeleted |
|---|---|
| 30 | 2025-11-02 12:49:22 |
| 75 | 2025-11-02 12:49:23 |
| 77 | 2025-11-02 12:49:24 |
| 81 | 2025-11-02 12:49:24 |
| 82 | 2025-11-02 12:49:24 |

## Table: `deletedSearches`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| savedSearchID | INTEGER | False | None | True |
| dateDeleted |  | True | CURRENT_TIMESTAMP | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `libraries`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| libraryID | INTEGER | False | None | True |
| type | TEXT | True | None | False |
| editable | INT | True | None | False |
| filesEditable | INT | True | None | False |
| version | INT | True | 0 | False |
| storageVersion | INT | True | 0 | False |
| lastSync | INT | True | 0 | False |
| archived | INT | True | 0 | False |

### Sample Data (first 5 rows)

| libraryID | type | editable | filesEditable | version | storageVersion | lastSync | archived |
|---|---|---|---|---|---|---|---|
| 1 | user | 1 | 1 | 927 | 927 | 1764232716 | 0 |
| 2 | group | 1 | 1 | 482 | 482 | 1764232716 | 0 |
| 3 | group | 1 | 1 | 474 | 474 | 1764232716 | 0 |

## Table: `users`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| userID | INTEGER | False | None | True |
| name | TEXT | True | None | False |

### Sample Data (first 5 rows)

| userID | name |
|---|---|
| 14083429 | philipplentzen |
| 14445519 | AlexKulibaba |

## Table: `groups`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| groupID | INTEGER | False | None | True |
| libraryID | INT | True | None | False |
| name | TEXT | True | None | False |
| description | TEXT | True | None | False |
| version | INT | True | None | False |

### Sample Data (first 5 rows)

| groupID | libraryID | name | description | version |
|---|---|---|---|---|
| 5560629 | 2 | Alex Kulibaba BA |  | 2 |
| 6265004 | 3 | FsSE-Seminar |  | 2 |

## Table: `groupItems`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INTEGER | False | None | True |
| createdByUserID | INT | False | None | False |
| lastModifiedByUserID | INT | False | None | False |

### Sample Data (first 5 rows)

| itemID | createdByUserID | lastModifiedByUserID |
|---|---|---|
| 22 | 14445519 | None |
| 23 | 14445519 | None |
| 24 | 14445519 | None |
| 25 | 14445519 | None |
| 26 | 14445519 | None |

## Table: `publicationsItems`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INTEGER | False | None | True |

### Sample Data (first 5 rows)

No data in this table.

## Table: `retractedItems`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INTEGER | False | None | True |
| data | TEXT | False | None | False |
| flag | INT | False | 0 | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `fulltextItems`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| itemID | INTEGER | False | None | True |
| indexedPages | INT | False | None | False |
| totalPages | INT | False | None | False |
| indexedChars | INT | False | None | False |
| totalChars | INT | False | None | False |
| version | INT | True | 0 | False |
| synced | INT | True | 0 | False |

### Sample Data (first 5 rows)

| itemID | indexedPages | totalPages | indexedChars | totalChars | version | synced |
|---|---|---|---|---|---|---|
| 2 | 17 | 17 | None | None | 722 | 1 |
| 5 | 19 | 19 | None | None | 722 | 1 |
| 6 | None | None | 3380 | 3380 | 722 | 1 |
| 8 | 10 | 10 | None | None | 722 | 1 |
| 9 | None | None | 3696 | 3696 | 722 | 1 |

## Table: `fulltextWords`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| wordID | INTEGER | False | None | True |
| word | TEXT | False | None | False |

### Sample Data (first 5 rows)

| wordID | word |
|---|---|
| 1 | 0 |
| 2 | 1 |
| 3 | 10 |
| 4 | 100 |
| 5 | 101 |

## Table: `fulltextItemWords`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| wordID | INT | False | None | True |
| itemID | INT | False | None | True |

### Sample Data (first 5 rows)

| wordID | itemID |
|---|---|
| 1 | 2 |
| 2 | 2 |
| 3 | 2 |
| 4 | 2 |
| 5 | 2 |

## Table: `syncCache`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| libraryID | INT | True | None | True |
| key | TEXT | True | None | True |
| syncObjectTypeID | INT | True | None | True |
| version | INT | True | None | True |
| data | TEXT | False | None | False |

### Sample Data (first 5 rows)

| libraryID | key | syncObjectTypeID | version | data |
|---|---|---|---|---|
| 1 | ALSTS8TI | 3 | 693 | {"key":"ALSTS8TI","version":693,"data":{"key":"ALSTS8TI","version":693,"itemType":"webpage","title":... [truncated] |
| 1 | N9PVDU2Q | 3 | 693 | {"key":"N9PVDU2Q","version":693,"data":{"key":"N9PVDU2Q","version":693,"itemType":"webpage","title":... [truncated] |
| 1 | LYY2JKBG | 3 | 368 | {"key":"LYY2JKBG","version":368,"data":{"key":"LYY2JKBG","version":368,"itemType":"journalArticle","... [truncated] |
| 1 | XJJLL3BR | 3 | 5 | {"key":"XJJLL3BR","version":5,"data":{"key":"XJJLL3BR","version":5,"itemType":"journalArticle","titl... [truncated] |
| 1 | P6IIVXFW | 3 | 369 | {"key":"P6IIVXFW","version":369,"data":{"key":"P6IIVXFW","version":369,"parentItem":"LYY2JKBG","item... [truncated] |

## Table: `syncDeleteLog`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| syncObjectTypeID | INT | True | None | False |
| libraryID | INT | True | None | False |
| key | TEXT | True | None | False |
| dateDeleted | TEXT | True | CURRENT_TIMESTAMP | False |

### Sample Data (first 5 rows)

| syncObjectTypeID | libraryID | key | dateDeleted |
|---|---|---|---|
| 7 | 1 | lastPageIndex_g6265004_F4HDHUET | 2025-11-12 14:10:26 |
| 7 | 1 | lastPageIndex_g6265004_NG4XAPWC | 2025-11-12 14:10:26 |
| 7 | 1 | lastPageIndex_g6265004_BDDKCEC3 | 2025-11-26 13:15:04 |
| 7 | 1 | lastPageIndex_g6265004_3GRH88IJ | 2025-11-26 13:15:04 |
| 7 | 1 | lastPageIndex_g6265004_4SZDRHX2 | 2025-11-26 13:15:04 |

## Table: `syncQueue`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| libraryID | INT | True | None | True |
| key | TEXT | True | None | True |
| syncObjectTypeID | INT | True | None | True |
| lastCheck | TIMESTAMP | False | None | False |
| tries | INT | False | None | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `storageDeleteLog`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| libraryID | INT | True | None | True |
| key | TEXT | True | None | True |
| dateDeleted | TEXT | True | CURRENT_TIMESTAMP | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `proxies`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| proxyID | INTEGER | False | None | True |
| multiHost | INT | False | None | False |
| autoAssociate | INT | False | None | False |
| scheme | TEXT | False | None | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `proxyHosts`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| hostID | INTEGER | False | None | True |
| proxyID | INTEGER | False | None | False |
| hostname | TEXT | False | None | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `relationPredicates`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| predicateID | INTEGER | False | None | True |
| predicate | TEXT | False | None | False |

### Sample Data (first 5 rows)

| predicateID | predicate |
|---|---|
| 1 | owl:sameAs |

## Table: `customItemTypes`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| customItemTypeID | INTEGER | False | None | True |
| typeName | TEXT | False | None | False |
| label | TEXT | False | None | False |
| display | INT | False | 1 | False |
| icon | TEXT | False | None | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `customFields`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| customFieldID | INTEGER | False | None | True |
| fieldName | TEXT | False | None | False |
| label | TEXT | False | None | False |

### Sample Data (first 5 rows)

No data in this table.

## Table: `customItemTypeFields`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| customItemTypeID | INT | True | None | True |
| fieldID | INT | False | None | False |
| customFieldID | INT | False | None | False |
| hide | INT | True | None | False |
| orderIndex | INT | True | None | True |

### Sample Data (first 5 rows)

No data in this table.

## Table: `customBaseFieldMappings`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| customItemTypeID | INT | False | None | True |
| baseFieldID | INT | False | None | True |
| customFieldID | INT | False | None | True |

### Sample Data (first 5 rows)

No data in this table.

## Table: `translatorCache`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| fileName | TEXT | False | None | True |
| metadataJSON | TEXT | False | None | False |
| lastModifiedTime | INT | False | None | False |

### Sample Data (first 5 rows)

| fileName | metadataJSON | lastModifiedTime |
|---|---|---|
| Polygon.js | {"translatorID":"fa7c37b1-fda4-418a-a8b8-2491929411ab","translatorType":4,"label":"Polygon","creator... [truncated] | 1262300400000 |
| The Art Newspaper.js | {"translatorID":"7ae2681a-185b-4724-8754-f046d96884c8","translatorType":4,"label":"The Art Newspaper... [truncated] | 1262300400000 |
| AIP.js | {"translatorID":"48d3b115-7e09-4134-ad5d-0beda6296761","translatorType":4,"label":"AIP","creator":"A... [truncated] | 1262300400000 |
| MCV.js | {"translatorID":"b51ac026-ed35-4c68-89bb-b42b1e1ce8f2","translatorType":4,"label":"MCV","creator":"c... [truncated] | 1262300400000 |
| Code4Lib Journal.js | {"translatorID":"a326fc49-60c2-405b-8f44-607e5d18b9ad","translatorType":4,"label":"Code4Lib Journal"... [truncated] | 1262300400000 |

## Table: `dbDebug1`

### Schema

| Column Name | Data Type | Not Null | Default Value | Primary Key |
|-------------|-----------|----------|---------------|-------------|
| a | INTEGER | False | None | True |

### Sample Data (first 5 rows)

No data in this table.

