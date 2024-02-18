## zh-CN

`block` 属性使其适合父元素宽度。

## en-US

`block` property will make the `Segmented` fit to its parent width.
```tsx
import React from 'react';
import { Segmented } from 'antd';

const Demo: React.FC = () => (
  <Segmented options={[123, 456, 'longtext-longtext-longtext-longtext']} block />
);

export default Demo;
```
