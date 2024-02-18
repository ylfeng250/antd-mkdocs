## zh-CN

允许自定义选择标签的样式。

## en-US

Allows for custom rendering of tags.
```tsx
import React from 'react';
import { Select, Tag } from 'antd';
import type { SelectProps } from 'antd';

type TagRender = SelectProps['tagRender'];

const options = [{ value: 'gold' }, { value: 'lime' }, { value: 'green' }, { value: 'cyan' }];

const tagRender: TagRender = (props) => {
  const { label, value, closable, onClose } = props;
  const onPreventMouseDown = (event: React.MouseEvent<HTMLSpanElement>) => {
    event.preventDefault();
    event.stopPropagation();
  };
  return (
    <Tag
      color={value}
      onMouseDown={onPreventMouseDown}
      closable={closable}
      onClose={onClose}
      style={{ marginRight: 3 }}
    >
      {label}
    </Tag>
  );
};

const App: React.FC = () => (
  <Select
    mode="multiple"
    tagRender={tagRender}
    defaultValue={['gold', 'cyan']}
    style={{ width: '100%' }}
    options={options}
  />
);

export default App;
```
