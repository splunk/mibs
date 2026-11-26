#
# PySNMP MIB module CISCO-RMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RMON-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-RMON-CAPABILITY", ciscoRmonCapCatOSV08R0101=ciscoRmonCapCatOSV08R0101, ciscoRmonCapNXOSV04R0101PMDS9000=ciscoRmonCapNXOSV04R0101PMDS9000, ciscoRmonCapability=ciscoRmonCapability, PYSNMP_MODULE_ID=ciscoRmonCapability)
