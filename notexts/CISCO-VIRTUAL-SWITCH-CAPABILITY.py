#
# PySNMP MIB module CISCO-VIRTUAL-SWITCH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VIRTUAL-SWITCH-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
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
mibBuilder.exportSymbols("CISCO-VIRTUAL-SWITCH-CAPABILITY", cvsCapV12R0233SXI4PCat6K=cvsCapV12R0233SXI4PCat6K, cvsCapV15R0001SYPCat6K=cvsCapV15R0001SYPCat6K, PYSNMP_MODULE_ID=ciscoVirtualSwitchCapability, cvsCapV15R0101SYPCat6K=cvsCapV15R0101SYPCat6K, cvsCapV12R0233SXH01PCat6K=cvsCapV12R0233SXH01PCat6K, ciscoVirtualSwitchCapability=ciscoVirtualSwitchCapability)
