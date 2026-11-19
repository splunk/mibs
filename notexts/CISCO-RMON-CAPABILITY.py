#
# PySNMP MIB module CISCO-RMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RMON-CAPABILITY
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
ciscoRmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 357))
ciscoRmonCapability.setRevisions(('2008-08-04 00:00', '2006-03-09 00:00', '2004-04-02 00:00',))
if mibBuilder.loadTexts: ciscoRmonCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoRmonCapability.setOrganization('Cisco Systems, Inc.')
ciscoRmonCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 357, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapCatOSV08R0101 = ciscoRmonCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapCatOSV08R0101 = ciscoRmonCapCatOSV08R0101.setStatus('current')
ciscoRmonCapNXOSV04R0101PMDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 357, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapNXOSV04R0101PMDS9000 = ciscoRmonCapNXOSV04R0101PMDS9000.setProductRelease('Cisco NX-OS 4.1(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapNXOSV04R0101PMDS9000 = ciscoRmonCapNXOSV04R0101PMDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-RMON-CAPABILITY", ciscoRmonCapCatOSV08R0101=ciscoRmonCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoRmonCapability, ciscoRmonCapability=ciscoRmonCapability, ciscoRmonCapNXOSV04R0101PMDS9000=ciscoRmonCapNXOSV04R0101PMDS9000)
