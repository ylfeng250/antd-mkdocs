## zh-CN

通过 `value` 和 `onChange` 设置组件为受控模式。

## en-US

Set the component to controlled mode.
```tsx
import React, { useState } from 'react';
import { ColorPicker } from 'antd';
import type { ColorPickerProps, GetProp } from 'antd';

type Color = GetProp<ColorPickerProps, 'value'>;

const Demo: React.FC = () => {
  const [color, setColor] = useState<Color>('#1677ff');
  return <ColorPicker value={color} onChange={setColor} />;
};

export default Demo;
```
