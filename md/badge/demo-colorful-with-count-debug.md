## zh-CN

在使用多彩徽标的同时，支持 count 属性显示

## en-US

support `count` when use colorful badge
```tsx
import React from 'react';
import { Badge, Space } from 'antd';

const colors = [
  'pink',
  'red',
  'yellow',
  'orange',
  'cyan',
  'green',
  'blue',
  'purple',
  'geekblue',
  'magenta',
  'volcano',
  'gold',
  'lime',
];

const AvatarItem = ({ color }: { color: string }) => (
  <div
    style={{
      width: 90,
      height: 90,
      lineHeight: '90px',
      background: '#ccc',
      textAlign: 'center',
    }}
  >
    {color}
  </div>
);

const App: React.FC = () => (
  <>
    <Space wrap size={['large', 'middle']}>
      {colors.map((color) => (
        <Badge color={color} count={44} key={color}>
          <AvatarItem color={color} />
        </Badge>
      ))}
    </Space>
    <Space wrap size={['large', 'middle']}>
      {colors.map((color) => (
        <Badge status="processing" color={color} text="loading" key={color} />
      ))}
    </Space>
  </>
);

export default App;
```
