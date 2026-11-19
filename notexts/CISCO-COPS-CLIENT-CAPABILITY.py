#
# PySNMP MIB module CISCO-COPS-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-COPS-CLIENT-CAPABILITY
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
ciscoCopsClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 313))
ciscoCopsClientCapability.setRevisions(('2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoCopsClientCapability.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: ciscoCopsClientCapability.setOrganization('Cisco Systems, Inc.')
ccopsClientCapCatOSV53R2Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 313, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV53R2Cat6k = ccopsClientCapCatOSV53R2Cat6k.setProductRelease('Cisco CatOS 5.3(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV53R2Cat6k = ccopsClientCapCatOSV53R2Cat6k.setStatus('current')
ccopsClientCapCatOSV61R1Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 313, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV61R1Cat6k = ccopsClientCapCatOSV61R1Cat6k.setProductRelease('Cisco CatOS 6.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV61R1Cat6k = ccopsClientCapCatOSV61R1Cat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-COPS-CLIENT-CAPABILITY", ciscoCopsClientCapability=ciscoCopsClientCapability, ccopsClientCapCatOSV53R2Cat6k=ccopsClientCapCatOSV53R2Cat6k, ccopsClientCapCatOSV61R1Cat6k=ccopsClientCapCatOSV61R1Cat6k, PYSNMP_MODULE_ID=ciscoCopsClientCapability)
