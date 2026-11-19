#
# PySNMP MIB module CISCO-HW-MODULE-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HW-MODULE-CONTROL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHwModuleControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 588))
ciscoHwModuleControlCapability.setRevisions(('2012-09-07 00:00', '2011-09-27 00:00', '2010-03-17 00:00',))
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setOrganization('Cisco Systems, Inc.')
chmcCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV12R0233SXI4PCat6K = chmcCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV12R0233SXI4PCat6K = chmcCapV12R0233SXI4PCat6K.setStatus('current')
chmcCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SYPCat6K = chmcCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SYPCat6K = chmcCapV15R0001SYPCat6K.setStatus('current')
chmcCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SY1PCat6K = chmcCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SY1PCat6K = chmcCapV15R0001SY1PCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-HW-MODULE-CONTROL-CAPABILITY", chmcCapV12R0233SXI4PCat6K=chmcCapV12R0233SXI4PCat6K, PYSNMP_MODULE_ID=ciscoHwModuleControlCapability, chmcCapV15R0001SY1PCat6K=chmcCapV15R0001SY1PCat6K, ciscoHwModuleControlCapability=ciscoHwModuleControlCapability, chmcCapV15R0001SYPCat6K=chmcCapV15R0001SYPCat6K)
