## zh-CN

可通过 `CheckableTag` 实现类似 Checkbox 的效果，点击切换选中效果。

> 该组件为完全受控组件，不支持非受控用法。

## en-US

`CheckableTag` works like Checkbox, click it to toggle checked state.

> it is an absolute controlled component and has no uncontrolled mode.
```tsx
import React, { useState } from 'react';
import { Space, Tag } from 'antd';

const { CheckableTag } = Tag;

const tagsData = ['Movies', 'Books', 'Music', 'Sports'];

const App: React.FC = () => {
  const [selectedTags, setSelectedTags] = useState<string[]>(['Books']);

  const handleChange = (tag: string, checked: boolean) => {
    const nextSelectedTags = checked
      ? [...selectedTags, tag]
      : selectedTags.filter((t) => t !== tag);
    console.log('You are interested in: ', nextSelectedTags);
    setSelectedTags(nextSelectedTags);
  };

  return (
    <>
      <span style={{ marginRight: 8 }}>Categories:</span>
      <Space size={[0, 8]} wrap>
        {tagsData.map((tag) => (
          <CheckableTag
            key={tag}
            checked={selectedTags.includes(tag)}
            onChange={(checked) => handleChange(tag, checked)}
          >
            {tag}
          </CheckableTag>
        ))}
      </Space>
    </>
  );
};

export default App;
```
