#
# PySNMP MIB module CISCO-ATM-TRUNK-STAT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ATM-TRUNK-STAT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
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
ciscoAtmTrunkStatCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 420))
ciscoAtmTrunkStatCapability.setRevisions(('2005-09-19 00:00', '2004-11-17 00:00', '2004-06-15 00:00',))
if mibBuilder.loadTexts: ciscoAtmTrunkStatCapability.setLastUpdated('200509190000Z')
if mibBuilder.loadTexts: ciscoAtmTrunkStatCapability.setOrganization('Cisco Systems, Inc.')
cAtmTrunkStatCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 420, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM33 = cAtmTrunkStatCapVISM33.setProductRelease('Cisco VISM Release 3.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM33 = cAtmTrunkStatCapVISM33.setStatus('current')
cAtmTrunkStatCapVISM3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 420, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM3325 = cAtmTrunkStatCapVISM3325.setProductRelease('Cisco VISM Release 3.3.25.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM3325 = cAtmTrunkStatCapVISM3325.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-TRUNK-STAT-CAPABILITY", cAtmTrunkStatCapVISM3325=cAtmTrunkStatCapVISM3325, PYSNMP_MODULE_ID=ciscoAtmTrunkStatCapability, cAtmTrunkStatCapVISM33=cAtmTrunkStatCapVISM33, ciscoAtmTrunkStatCapability=ciscoAtmTrunkStatCapability)
