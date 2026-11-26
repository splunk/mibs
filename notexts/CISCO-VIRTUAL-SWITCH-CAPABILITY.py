#
# PySNMP MIB module CISCO-VIRTUAL-SWITCH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VIRTUAL-SWITCH-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVirtualSwitchCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 563))
ciscoVirtualSwitchCapability.setRevisions(('2012-09-07 00:00', '2011-09-26 00:00', '2010-03-29 00:00', '2008-01-14 00:00',))
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setOrganization('Cisco Systems, Inc.')
cvsCapV12R0233SXH01PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXH01PCat6K = cvsCapV12R0233SXH01PCat6K.setProductRelease('Cisco IOS 12.2(33)SXH1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXH01PCat6K = cvsCapV12R0233SXH01PCat6K.setStatus('current')
cvsCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXI4PCat6K = cvsCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXI4PCat6K = cvsCapV12R0233SXI4PCat6K.setStatus('current')
cvsCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0001SYPCat6K = cvsCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0001SYPCat6K = cvsCapV15R0001SYPCat6K.setStatus('current')
cvsCapV15R0101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0101SYPCat6K = cvsCapV15R0101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0101SYPCat6K = cvsCapV15R0101SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-VIRTUAL-SWITCH-CAPABILITY", cvsCapV12R0233SXH01PCat6K=cvsCapV12R0233SXH01PCat6K, PYSNMP_MODULE_ID=ciscoVirtualSwitchCapability, ciscoVirtualSwitchCapability=ciscoVirtualSwitchCapability, cvsCapV12R0233SXI4PCat6K=cvsCapV12R0233SXI4PCat6K, cvsCapV15R0101SYPCat6K=cvsCapV15R0101SYPCat6K, cvsCapV15R0001SYPCat6K=cvsCapV15R0001SYPCat6K)
