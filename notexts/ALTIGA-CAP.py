#
# PySNMP MIB module ALTIGA-CAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-CAP
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
alCapModule, altigaCaps = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alCapModule", "altigaCaps")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaCapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 2, 1))
altigaCapModule.setRevisions(('2002-09-09 12:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaCapModule.setLastUpdated('200209091200Z')
if mibBuilder.loadTexts: altigaCapModule.setOrganization('Cisco Systems, Inc.')
altigaBasicAgent = AgentCapabilities((1, 3, 6, 1, 4, 1, 3076, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgent = altigaBasicAgent.setProductRelease('Altiga Agent v1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgent = altigaBasicAgent.setStatus('obsolete')
altigaBasicAgentRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 3076, 1, 1, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgentRev1 = altigaBasicAgentRev1.setProductRelease('Altiga Agent v1.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgentRev1 = altigaBasicAgentRev1.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-CAP", altigaCapModule=altigaCapModule, altigaBasicAgentRev1=altigaBasicAgentRev1, altigaBasicAgent=altigaBasicAgent, PYSNMP_MODULE_ID=altigaCapModule)
